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
[GraphicsSettings](Rendering.GraphicsSettings.html).lightsUseLinearIntensity

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

public static bool lightsUseLinearIntensity;

### Description

If this is true, Light intensity is multiplied against linear color values. If
it is false, gamma color values are used.

Light intensity is multiplied by the linear color value when
lightsUseLinearIntensity is enabled. This is physically correct but not the
default for 3D projects created with Unity 5.6 and newer. By default
[lightsUseLinearIntensity](Rendering.GraphicsSettings-
lightsUseLinearIntensity.html) is set to false.  
  
2D projects will have [lightsUseLinearIntensity](Rendering.GraphicsSettings-
lightsUseLinearIntensity.html) set to disabled by default. When disabled, the
gamma color value is multiplied with the intensity. If you want to use
[lightsUseColorTemperature](Rendering.GraphicsSettings-
lightsUseColorTemperature.html),
[lightsUseLinearIntensity](Rendering.GraphicsSettings-
lightsUseLinearIntensity.html) has to be enabled.  
  
If you enable [lightsUseLinearIntensity](Rendering.GraphicsSettings-
lightsUseLinearIntensity.html) on an existing project, all your Lights will
need to be tweaked to regain their original look.  
  
Additional resources:
[GraphicsSettings.lightsUseColorTemperature](Rendering.GraphicsSettings-
lightsUseColorTemperature.html), [Light.colorTemperature](Light-
colorTemperature.html).

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

