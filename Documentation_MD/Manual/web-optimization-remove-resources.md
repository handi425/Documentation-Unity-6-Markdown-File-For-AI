[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/web-optimization-remove-resources.html)
  * [中文](/cn/current/Manual/web-optimization-remove-resources.html)
  * [日本語](/ja/current/Manual/web-optimization-remove-resources.html)
  * [한국어](/kr/current/Manual/web-optimization-remove-resources.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/web-optimization-remove-resources.html)
  * [中文](/cn/current/Manual/web-optimization-remove-resources.html)
  * [日本語](/ja/current/Manual/web-optimization-remove-resources.html)
  * [한국어](/kr/current/Manual/web-optimization-remove-resources.html)

  * [Platform development ](PlatformSpecific.html)
  * [Web](webgl.html)
  * [Build and distribute a Web application](webgl-building-distribution.html)
  * [Optimize your Web build](web-optimization.html)
  * Remove unused resources from your Web build

[](web-optimization-c-sharp.html)

Use C# code to enable optimization settings

[](web-optimization-mobile.html)

Optimize Web platform for mobile

# Remove unused resources from your Web build

Remove unused packages and **shaders** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) from a project to make the build
smaller. A smaller build reduces application load times and improves the
performance of your application.

## Remove or disable unused packages

Unused packages might affect the final output size of the build. Remove or
disable all packages the project doesn’t use. This includes **built-in
packages** _Built-in_ packages allow users to toggle Unity features on or off
through the Package Manager. Enabling or disabling a package reduces the run-
time build size. For example, most projects don’t use the legacy Particle
System. By removing the abstracted package of this feature, the related code
and resources are not part of the final built product. Typically, these
packages contain only the package manifest and are bundled with Unity (rather
than available on the package registry).  
See in [Glossary](Glossary.html#Built-inpackage) and packages enabled by
default, such as the [Input System
package](https://docs.unity3d.com/Packages/com.unity.inputsystem@latest?subfolder=/manual/index.html),
which can double the build size if it’s not removed.

To remove a package, refer to [Remove a UPM package from a project](upm-ui-
remove.html).

To disable a built-in package, refer to [Disable a built-in package](upm-ui-
disable.html).

## Remove unused shader variants

Enable shader stripping to remove shader variants that aren’t used in a
**scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). Shader stripping can reduce your build
file size.

**Important** : Test your application to make sure your unused shaders aren’t
referenced by other shaders.

To enable shader stripping, refer to [Graphics](class-
GraphicsSettings.html#stripping).

## Additional resources

  * [Optimize your Web build](web-optimization.html)
  * [Recommended Graphics settings to optimize your Web build](web-optimization-graphics.html)
  * [Recommended Quality settings to optimize your Web build](web-optimization-quality.html)
  * [Recommended Player settings to optimize your Web build](web-optimization-player.html)
  * [Optimize Web platform for mobile](web-optimization-mobile.html)

[](web-optimization-c-sharp.html)

Use C# code to enable optimization settings

[](web-optimization-mobile.html)

Optimize Web platform for mobile

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

