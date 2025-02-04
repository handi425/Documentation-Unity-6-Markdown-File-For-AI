[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/override-player-settings.html)
  * [中文](/cn/current/Manual/override-player-settings.html)
  * [日本語](/ja/current/Manual/override-player-settings.html)
  * [한국어](/kr/current/Manual/override-player-settings.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/override-player-settings.html)
  * [中文](/cn/current/Manual/override-player-settings.html)
  * [日本語](/ja/current/Manual/override-player-settings.html)
  * [한국어](/kr/current/Manual/override-player-settings.html)

  * [The Unity Editor](unity-editor.html)
  * [Editor Features](EditorFeatures.html)
  * [Build profiles](BuildSettings.html)
  * Override Player settings with build profiles

[](build-profile-scene-list.html)

Manage scenes in your build

[](build-profiles-reference.html)

Build Profiles window reference

# Override Player settings with build profiles

You can override Player settings when using a build profile for your target
platform. This allows you to have custom Player settings for each build
profile you want to use.

## Override Player settings

To override Player settings, use the following steps:

  1. Navigate to **File** > **Build Profiles**.
  2. Select or create a build profile for your target platform. For information on how to create a build profile, refer to [Create a build profile](create-build-profile.html).
  3. In the **Player Settings Overrides** section, select **Customize player settings**.

The [Player settings](class-PlayerSettings.html)Settings that let you set
various player-specific options for the final game built by Unity. [More
info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings) for the build profile’s target
platform will appear, allowing you to customize them as required. These Player
settings inherit their initial values from the global target platform Player
settings, available from **Edit** > **Project Settings** > **Player** > **<
Target Platform>**.

**Note** : You can only override Player settings for build profiles. If you
want to override Player settings for a platform profile, you must create a
build profile for that target.

## Remove and reset Player settings overrides

You can remove and reset any overridden Player settings for your build profile
using the available options from the **More** (**⋮**) menu. The available
options are as follows:

**Property** | **Description**  
---|---  
**Remove Overrides** | Remove and reset all overridden Player settings. To add new overrides, you must select **Customize player settings**.  
**Reset To Globals** | Reset overridden Player setting values to the global values for the target platform. The global values can be updated from **Edit** > **Project Settings** > **Player**  
  
## Additional resources

  * [Build profiles](build-profiles.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)  
See in [Glossary](Glossary.html#Buildprofile)

  * [Create a build profile](create-build-profile.html)
  * [Player settings](class-PlayerSettings.html)

[](build-profile-scene-list.html)

Manage scenes in your build

[](build-profiles-reference.html)

Build Profiles window reference

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

