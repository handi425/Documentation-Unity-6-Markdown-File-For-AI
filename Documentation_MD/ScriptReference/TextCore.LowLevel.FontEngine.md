[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# FontEngine

class in UnityEngine.TextCore.LowLevel

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

The FontEngine is used to access data from source font files. This includes
information about individual characters, glyphs and relevant metrics typically
used in the process of text parsing, layout and rendering.  
  
The types of font files supported are TrueType (.ttf, .ttc) and OpenType
(.otf).  
  
The FontEngine is also used to raster the visual representation of characters
known as glyphs in a given font atlas texture.

### Static Methods

[DestroyFontEngine](TextCore.LowLevel.FontEngine.DestroyFontEngine.html)|
Destroy and unload resources used by the Font Engine.  
---|---  
[GetFaceInfo](TextCore.LowLevel.FontEngine.GetFaceInfo.html)| Get the FaceInfo
for the currently loaded and sized typeface.  
[GetFontFaces](TextCore.LowLevel.FontEngine.GetFontFaces.html)| Gets the font
faces and styles for the currently loaded font.  
[GetSystemFontNames](TextCore.LowLevel.FontEngine.GetSystemFontNames.html)|
Gets the family and style names of the system fonts.  
[InitializeFontEngine](TextCore.LowLevel.FontEngine.InitializeFontEngine.html)|
Initialize the Font Engine and required resources.  
[LoadFontFace](TextCore.LowLevel.FontEngine.LoadFontFace.html)| Load a source
font file.  
[SetFaceSize](TextCore.LowLevel.FontEngine.SetFaceSize.html)| Set the size of
the currently loaded font face.  
[TryGetGlyphIndex](TextCore.LowLevel.FontEngine.TryGetGlyphIndex.html)| Try to
get the glyph index for the character at the given Unicode value.  
[TryGetGlyphWithIndexValue](TextCore.LowLevel.FontEngine.TryGetGlyphWithIndexValue.html)|
Try loading the glyph for the given index value and if available populate the
glyph.  
[TryGetGlyphWithUnicodeValue](TextCore.LowLevel.FontEngine.TryGetGlyphWithUnicodeValue.html)|
Try loading a glyph for the given unicode value. If available, populates the
glyph and returns true. Otherwise returns false and populates the glyph with
the .notdef / missing glyph data.  
[UnloadAllFontFaces](TextCore.LowLevel.FontEngine.UnloadAllFontFaces.html)|
Unloads all currently loaded font faces and removes them from the cache.  
[UnloadFontFace](TextCore.LowLevel.FontEngine.UnloadFontFace.html)| Unloads
current font face and removes it from the cache.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

