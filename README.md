# ISOPOD RIDER

A browser downhill game. Four tracks: The Quarry, Baja Beach, Main Street and The Sandlot.

## Play
https://isopodkeepers.github.io/Isopod-Rider/isopod-rider.html

Controls: **UP** gas · **SPACE** load / brake · **LEFT / RIGHT** lean · **R** restart · **M** music · **]** skip song

## What's in here
| Path | What it is |
| --- | --- |
| `isopod-rider.html` | The whole game: code, levels, physics. This is the file you edit. |
| `assets/` | Pictures: backgrounds and props (bus, tube, swings, bike rack, billboard). |
| `music/` | The three songs on the playlist. |
| `tools/bundle.py` | Packs everything back into one stand-alone HTML file for sharing. |

The pictures and music used to be packed inside the HTML, which made it 8.6 MB.
Keeping them in folders makes the game file ~0.2 MB, small enough to open in the
GitHub editor or hand to an AI assistant in one piece.

## Playing offline / sharing
- **Folder version:** on GitHub click **Code → Download ZIP**, unzip, double-click
  `isopod-rider.html`. Keep `assets/` and `music/` next to it.
- **One-file version:** run `python3 tools/bundle.py`. It writes
  `isopod-rider-bundled.html`, which works on its own with nothing else.

## Editing
1. Open `isopod-rider.html` on GitHub and click the pencil icon.
2. Make the change and click **Commit changes**, with a one-line note on what you changed.
3. Wait about a minute, then reload the play link.

Every version is kept in **History**, so nothing is ever lost.
