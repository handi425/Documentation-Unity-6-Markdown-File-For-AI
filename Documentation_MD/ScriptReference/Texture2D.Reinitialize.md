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

#  [Texture2D](Texture2D.html).Reinitialize

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

## Declaration

public bool Reinitialize(int width, int height);

## Declaration

public bool Reinitialize(int width, int height,
[Experimental.Rendering.GraphicsFormat](Experimental.Rendering.GraphicsFormat.html)
format, bool hasMipMap);

## Declaration

public bool Reinitialize(int width, int height,
[TextureFormat](TextureFormat.html) format, bool hasMipMap);

### Parameters

width | The new width of the texture.  
---|---  
height | The new height of the texture.  
format | The new format of the texture.  
hasMipMap | Whether the texture reserves memory for a full mipmap chain.  
  
### Returns

**bool** `true` if the reinitialization was a success.

### Description

Reinitializes a Texture2D, making it possible for you to replace `width`,
`height`, `textureformat`, and `graphicsformat` data for that texture.

This action also clears the pixel data associated with the texture from the
CPU and GPU.  
  
This function is very similar to the [Texture](Texture.html) constructor,
except it works on a Texture object that already exists rather than creating a
new one.  
  
It is not possible to reinitialize **Crunched** textures, so if you pass a
**Crunched** texture to this method, it returns `false`. See [texture
formats](../Manual/texture-compression-formats.html) for more information
about compressed and crunched textures.  
  
Call [Apply](Texture2D.Apply.html) to upload the changed pixels to the
graphics card.  
  
[Texture.isReadable](Texture-isReadable.html) must be `true`.  
  
`Texture2D.Reinitialize` does not automatically update the [special texture
properties](../Manual/SL-PropertiesInPrograms.html) {TextureName}`_TexelSize`
and {TextureName}`_HDR`, which Unity sets automatically on shaders and
materials that use the texture. After using `Texture2D.Reinitialize`, you
should update {TextureName}`_TexelSize` and {TextureName}`_HDR` on your
material or shader if you need them.

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

