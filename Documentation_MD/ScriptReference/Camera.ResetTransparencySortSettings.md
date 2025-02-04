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

#  [Camera](Camera.html).ResetTransparencySortSettings

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

[Switch to Manual](../Manual/class-Camera.html "Go to Camera Component in the
Manual")

## Declaration

public void ResetTransparencySortSettings();

### Description

Resets this Camera's transparency sort settings to the default. Default
transparency settings are taken from
[GraphicsSettings](Rendering.GraphicsSettings.html) instead of directly from
this Camera.

The rendering pipeline will, by default, take the transparency sort settings
from [GraphicsSettings](Rendering.GraphicsSettings.html). This is very
convenient and caters to most use cases. However, if you have the need to
alter the settings per Camera, you may do so with the [Camera](Camera.html)'s
APIs.  
  
Once [Camera.transparencySortMode](Camera-transparencySortMode.html) or
[Camera.transparencySortAxis](Camera-transparencySortAxis.html) are called
from the script, the rendering pipeline ignores the settings in the
[GraphicsSettings](Rendering.GraphicsSettings.html) and takes the settings
directly from the Camera.  
  
Calling this method causes the rendering pipeline to refer to the settings in
[GraphicsSettings](Rendering.GraphicsSettings.html) instead of this Camera.  
  
This works the same for SceneView Cameras as well.

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

