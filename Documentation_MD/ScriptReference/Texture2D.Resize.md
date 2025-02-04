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

**Method group is Obsolete**  

#  [Texture2D](Texture2D.html).Resize

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

**Obsolete** Texture2D.Resize(int, int, TextureFormat, bool) has been
deprecated because it actually reinitializes the texture. Use
Texture2D.Reinitialize(int, int, TextureFormat, bool) instead.  
**Upgrade to[Boolean)](System.Boolean\).html)**

## Declaration

public bool Resize(int width, int height, [TextureFormat](TextureFormat.html)
format, bool hasMipMap);

### Description

Resizes the texture.

Obsolete: Use [Texture2D.Reinitialize](Texture2D.Reinitialize.html) instead.  
  
Changes size of texture to `width` by `height`, format to `textureFormat` and
optionally creates mipmaps. After resizing, texture pixels will be undefined.
This function is very similar to the texture constructor, except it works on
existing texture object.  
  
Call [Apply](Texture2D.Apply.html) to actually upload the changed pixels to
the graphics card.  
  
[Texture.isReadable](Texture-isReadable.html) must be `true`.  
  
Note that Resize does not automatically update the [special texture
properties](../Manual/SL-PropertiesInPrograms.html) {TextureName}`_TexelSize`
and {TextureName}`_HDR` that are set automatically on shaders and materials
that use the texture. After using Resize, you should update these properties
manually on your material/shader if you need them.

* * *

**Obsolete** Texture2D.Resize(int, int) has been deprecated because it
actually reinitializes the texture. Use Texture2D.Reinitialize(int, int)
instead.  
**Upgrade to[Reinitialize](Texture2D.Reinitialize.html)**

## Declaration

public bool Resize(int width, int height);

### Description

Resizes the texture.

Changes size of texture to `width` by `height`. After resizing, texture pixels
will be undefined. This function is very similar to texture constructor,
except it works on existing texture object.  
  
Call [Apply](Texture2D.Apply.html) to actually upload the changed pixels to
the graphics card.  
  
[Texture.isReadable](Texture-isReadable.html) must be `true`.  
  
Note that Resize does not automatically update the [special texture
properties](../Manual/SL-PropertiesInPrograms.html) {TextureName}`_TexelSize`
and {TextureName}`_HDR` that are set automatically on shaders and materials
that use the texture. After using Resize, you should update these properties
manually on your material/shader if you need them.

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

