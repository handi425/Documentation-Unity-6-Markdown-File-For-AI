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

Virtual Texturing is experimental and not ready for production use. The
feature and documentation might be changed or removed in the future.

#  [Streaming](Rendering.VirtualTexturing.Streaming.html).GetTextureStackSize

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

public static void GetTextureStackSize([Material](Material.html) mat, int
stackNameId, out int width, out int height);

### Parameters

mat | The Material that contains the Virtual Texture Stack. The Virtual Texture Stacks contained in a Material are declared in the Material's Shader.  
---|---  
stackNameId | The unique identifier for the name of the Virtual Texture Stack, as declared in the Shader. To find the identifier for a given Shader property name, use [Shader.PropertyToID](Shader.PropertyToID.html).  
width | Unity populates `width` with the width of the Virtual Texture Stack, in pixels.  
height | Unity populates `height` with the height of the Virtual Texture Stack, in pixels.  
  
### Description

Gets the width and height of a Virtual Texture Stack, in pixels.

The width and height of a Virtual Texture Stack are usually based on the width
and height of the Textures assigned to the Material; however, various factors
can cause the width and height of a Virtual Texture Stack to differ from the
width and height of its Textures. Use this method to get the current width and
height of a Virtual Texture Stack, in pixels.  
  
Use this function to perform logic based on the width and height of the
Virtual Texture Stack, such as calculating a mip level.  
  
The width and height of a Virtual Texture Stack are constant for a given set
of Textures. If you change the Textures assigned to the Material, the width
and height of the Virtual Texture Stack might change.  
  
If you pass invalid data to this method, such as a null Material or an invalid
identifier, Unity will throw an exception and the values of `width` and
`height` will remain unmodified.

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

