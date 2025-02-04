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

#  [EditorCameraUtils](Rendering.EditorCameraUtils.html).RenderToCubemap

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

public static bool RenderToCubemap([Camera](Camera.html) camera,
[Texture](Texture.html) target, int faceMask,
[StaticEditorFlags](StaticEditorFlags.html) culledFlags);

### Parameters

camera | The Camera to use during rendering.  
---|---  
target | The cubemap to render to.  
faceMask | A bitmask which determines which of the six faces to render to.  
culledFlags | The flags of objects to cull during rendering.  
  
### Returns

**bool** If the render process succeeds, returns `true`. Otherwise, returns
`false`.

### Description

Renders this Camera into a static cubemap.

This function is mostly useful in the editor for "baking" static cubemaps of
your Scene.  
  
This functions uses the Camera's Clear Flags, its Transform’s Position, and
its Clipping Plane distances to render sections of the Scene into each cubemap
face. `faceMask` is a bitfield indicating which cubemap faces to render into.
Each set bit corresponds to a face. Bit numbers are integer values of
[CubemapFace](CubemapFace.html) enum type. By default, this process renders to
all six cubemap faces (the default value of 63 means the lowest six bits are
set. `false`). This function returns `false` if rendering to the cubemap
fails. An example of how this could happen is that some graphics hardware does
not support this functionality. Note: ReflectionProbes are a more advanced
method of performing real-time reflections. Note: You can create cubemaps in
the Editor by navigating to **Assets >Create>Legacy** and selecting
**Cubemap** option.  
  
Additional resources: [Cubemap assets](../Manual/class-Cubemap.html),
[Reflective shaders](../Manual/shader-ReflectiveFamily.html).

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

