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

#  [Texture](Texture.html).isReadable

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

public bool isReadable;

### Description

Whether Unity stores an additional copy of this texture's pixel data in CPU-
addressable memory.

This is required for methods that read, write, and manipulate the pixel data
on the CPU, such as [Texture2D.GetPixels](Texture2D.GetPixels.html) or
[ImageConversion.EncodeToPNG](ImageConversion.EncodeToPNG.html). It is not
required for methods that perform all their work on the GPU, such as
[Graphics.CopyTexture](Graphics.CopyTexture.html) or
[Graphics.Blit](Graphics.Blit.html).  
  
By default, this is `false` for texture assets that you import into your
project. To toggle this, use the **Read/Write Enabled** setting in the
[Texture Import Settings](../Manual/class-TextureImporter.html), or set
[TextureImporter.isReadable](TextureImporter-isReadable.html).  
  
By default, this is `true` when you create a texture from a script.  
  
**Note:** Readable textures use more memory than non-readable textures. You
should only make a texture readable when you need to, and you should make
textures non-readable when you are done working with the data on the CPU.  
  
To make a texture non-readable at runtime, call the `Apply` method for your
type of texture, for example [Texture2D.Apply](Texture2D.Apply.html) or
[Cubemap.Apply](Cubemap.Apply.html) and set the `makeNoLongerReadable`
parameter to `true`.

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

