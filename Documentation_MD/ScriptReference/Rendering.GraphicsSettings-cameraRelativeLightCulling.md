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

#
[GraphicsSettings](Rendering.GraphicsSettings.html).cameraRelativeLightCulling

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

public static bool cameraRelativeLightCulling;

### Description

Enable or disable using the camera position as the reference point for culling
lights.

When Unity culls distant lights, a light that's far away from the world space
origin can flicker. The flickering happens because GameObject coordinates
become increasingly less precise as they get further away, so the light moves
in and out of culling range.  
  
If you set `cameraRelativeLightCulling` to `true`, Unity uses the camera
position as the reference point for culling lights instead of the world space
origin. This can reduce flickering.  
  
If a light is closer to the world space origin than the camera position,
setting `cameraRelativeLightCulling` to `true` may introduce flickering or
make it worse. You can use the following approaches instead:

  * Reduce [Camera.farClipPlane](Camera-farClipPlane.html) to avoid the distance of lights becoming too large for precise calculations.
  * Make everything in your scene smaller, to reduce distances across your whole scene.

Additional resources:
[GraphicsSettings.cameraRelativeShadowCulling](Rendering.GraphicsSettings-
cameraRelativeShadowCulling.html)

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

