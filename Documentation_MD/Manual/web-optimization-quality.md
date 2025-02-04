[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/web-optimization-quality.html)
  * [中文](/cn/current/Manual/web-optimization-quality.html)
  * [日本語](/ja/current/Manual/web-optimization-quality.html)
  * [한국어](/kr/current/Manual/web-optimization-quality.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/web-optimization-quality.html)
  * [中文](/cn/current/Manual/web-optimization-quality.html)
  * [日本語](/ja/current/Manual/web-optimization-quality.html)
  * [한국어](/kr/current/Manual/web-optimization-quality.html)

  * [Platform development ](PlatformSpecific.html)
  * [Web](webgl.html)
  * [Build and distribute a Web application](webgl-building-distribution.html)
  * [Optimize your Web build](web-optimization.html)
  * Recommended Quality settings to optimize your Web build

[](web-optimization-player.html)

Recommended Player settings to optimize your Web build

[](web-optimization-c-sharp.html)

Use C# code to enable optimization settings

# Recommended Quality settings to optimize your Web build

Use the following recommended **Quality** settings to optimize your builds for
the Unity Web platform.

Configure the following recommended settings in **Edit** > **Project
Settings** > **Quality**. For more information on these settings, refer to
[Quality](class-QualitySettings.html).

## Quality Level

The **Quality** settings contain a group of possible **Quality Levels** for
your build. If you set your **Quality Level** to a lower setting (**Very Low**
or **Low**), it results in faster load times and better performance which is
recommended for a Web application. However, lower quality can mean the visuals
don’t look as good.

For more information about this setting, refer to [Quality](class-
QualitySettings.html).

### Change the Quality Level via C# code

To change the **Quality Level** via script instead, add this code to one of
your **scripts** A piece of code that allows you to create your own
Components, trigger game events, modify Component properties over time and
respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts):

    
    
    QualitySettings.SetQualityLevel(0, true); // Use the index of your quality settings matrix (0 = Very Low, 1 =  Low). 
    

## Additional resources

  * [Optimize your Web build](web-optimization.html)

  * [Recommended Graphics settings to optimize your Web build](web-optimization-graphics.html)

  * [Recommended Player settings to optimize your Web build](web-optimization-player.html)

  * [Remove unused resources from your Web build](web-optimization-remove-resources.html)

  * [Optimize Web platform for mobile](web-optimization-mobile.html)

[](web-optimization-player.html)

Recommended Player settings to optimize your Web build

[](web-optimization-c-sharp.html)

Use C# code to enable optimization settings

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

