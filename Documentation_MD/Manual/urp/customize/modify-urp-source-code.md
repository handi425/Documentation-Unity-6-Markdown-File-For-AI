[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/customize/modify-urp-source-code.html)
  * [中文](/cn/current/Manual/urp/customize/modify-urp-source-code.html)
  * [日本語](/ja/current/Manual/urp/customize/modify-urp-source-code.html)
  * [한국어](/kr/current/Manual/urp/customize/modify-urp-source-code.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/customize/modify-urp-source-code.html)
  * [中文](/cn/current/Manual/urp/customize/modify-urp-source-code.html)
  * [日本語](/ja/current/Manual/urp/customize/modify-urp-source-code.html)
  * [한국어](/kr/current/Manual/urp/customize/modify-urp-source-code.html)

  * [Lighting](../../LightingOverview.html)
  * [Lighting in URP](../../urp/lighting-landing.html)
  * [Custom lighting in URP](../../urp/lighting/custom-lighting-landing.html)
  * Modify URP lighting source code

[](../../urp/lighting/custom-lighting-change-light-falloff.html)

Change how lights fade using light falloff in URP

[](../../urp/universal-additional-light-data.html)

Universal Additional Light Data component in URP

# Modify URP lighting source code

For advanced rendering or lighting customizations, it might not be enough to
extend or override APIs defined in URP. You might need to modify URP source
code to change certain methods.

To prepare URP source code for modifications:

  1. In the root folder of your project, go to `Library/PackageCache`.

  2. Copy the following folders into the `Packages` folder at the root of your project:
    
        com.unity.render-pipelines.universal
    com.unity.render-pipelines.universal-config
    

Now Unity uses the URP source code from the `Packages` folder of your project,
and you can make changes to that code.

## Plan the upgrade process

After you copy the URP source code into the `Packages` folder, this code
becomes part of your project and is no longer part of a Unity install. If you
upgrade the Unity version later, Unity doesn’t update the URP source
automatically. You need to apply the changes to source code manually.

To make this process easier, document all the changes you make to the URP
source code in your project.

## Additional resources

  * [Custom lighting in URP](../lighting/custom-lighting-landing.html)

[](../../urp/lighting/custom-lighting-change-light-falloff.html)

Change how lights fade using light falloff in URP

[](../../urp/universal-additional-light-data.html)

Universal Additional Light Data component in URP

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

