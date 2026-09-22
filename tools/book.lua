-- Numbers chapters as "第 N 章" and figures as "图 N-M", inserts the part pages listed in
-- metadata.yaml, and keeps each chapter's "本章提到的资料" section out of the table of contents.

local function has(classes, name)
  for _, c in ipairs(classes) do
    if c == name then return true end
  end
  return false
end

function Pandoc(doc)
  local parts = {}
  for _, p in ipairs(doc.meta.parts or {}) do
    parts[tonumber(pandoc.utils.stringify(p.chapter))] = p
  end

  local blocks, n = pandoc.Blocks({}), 0
  for _, b in ipairs(doc.blocks) do
    if b.t == "Header" and b.level == 1 and not has(b.classes, "unnumbered") then
      n = n + 1
      local p = parts[n]
      if p then
        blocks:insert(pandoc.Header(1, p.title, pandoc.Attr("part-" .. n, {"part", "unnumbered"})))
        if p.intro then blocks:insert(pandoc.Para(p.intro)) end
      end
      b.content = pandoc.Inlines("第 " .. n .. " 章") .. {pandoc.Space()} .. b.content
    elseif b.t == "Header" and b.level == 2 and pandoc.utils.stringify(b.content) == "本章提到的资料" then
      b.classes:insert("unlisted")
    end
    blocks:insert(b)
  end
  doc.blocks = blocks

  -- Number figures as 图 N-M, including figures nested in lists.
  local chapter, figure = 0, 0
  doc = doc:walk({
    traverse = "topdown",
    Header = function(h)
      if h.level == 1 and not has(h.classes, "unnumbered") then
        chapter = chapter + 1
        figure = 0
      end
    end,
    Figure = function(f)
      if chapter == 0 then return nil end
      figure = figure + 1
      local first = f.caption.long[1]
      if first then
        first.content = pandoc.Inlines("图 " .. chapter .. "-" .. figure .. "\u{3000}") .. first.content
      end
      return f
    end,
  })
  return doc
end

function Image(img)
  if FORMAT:match("html") then
    img.attributes.loading = "lazy"
  end
  return img
end
