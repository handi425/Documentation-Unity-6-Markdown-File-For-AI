[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/URP-Config-Package.html)
  * [中文](/cn/current/Manual/urp/URP-Config-Package.html)
  * [日本語](/ja/current/Manual/urp/URP-Config-Package.html)
  * [한국어](/kr/current/Manual/urp/URP-Config-Package.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/URP-Config-Package.html)
  * [中文](/cn/current/Manual/urp/URP-Config-Package.html)
  * [日本語](/ja/current/Manual/urp/URP-Config-Package.html)
  * [한국어](/kr/current/Manual/urp/URP-Config-Package.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Render pipelines](../render-pipelines.html)
  * [Using the Universal Render Pipeline](../universal-render-pipeline.html)
  * [Graphics quality settings in URP](../urp/urp-quality-settings-landing.html)
  * Configure settings with the URP Config package

[](../urp/quality/change-urp-asset-settings.html)

Change URP Asset settings at runtime

[](../urp/anti-aliasing.html)

Add anti-aliasing in the Universal Render Pipeline

# Configure settings with the URP Config package

You can use the Universal **Render Pipeline** A series of operations that take
the contents of a Scene, and displays them on a screen. Unity lets you choose
from pre-built render pipelines, or write your own. [More info](../render-
pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP) Config package to
control some of the settings of URP. Unity automatically adds the package
files in the package cache as they are a dependency of URP, but you must make
a copy of them in your project before you can use the package.

The URP Config Package currently only changes one setting which is the maximum
number of visible lights URP renders when you use the Forward+ **Rendering
Path** The technique that a render pipeline uses to render graphics. Choosing
a different rendering path affects how lighting and shading are calculated.
Some rendering paths are more suited to different platforms and hardware than
others. [More info](../RenderingPaths.html)  
See in [Glossary](../Glossary.html#RenderingPath). For more information, refer
to [Change the maximum number of visible lights](rendering/forward-plus-
rendering-path-limitations.html).

## Set up the URP Config package

To create a usable copy of the URP Config package in your project, do the
following:

  1. In the **Project** window, right-click **Assets** and select **Show in Explorer** (MacOS: **Reveal in Finder**).
  2. Go to `/Library/PackageCache/`.
  3. Copy the `com.unity.render-pipelines.universal-config` folder to the `Packages` folder.

The URP Config package is now ready for use in your project.

## Configure URP with the URP Config package

You can edit the `ShaderConfig.cs` file to configure the properties of your
URP project. If you edit this file, you must also update the equivalent
`ShaderConfig.cs.hlsl` header file so that it mirrors the definitions you set
in `ShaderConfig.cs`.

You can update the `ShaderConfig.cs.hlsl` file in two ways:

  * Manually edit the `ShaderConfig.cs.hlsl` file to mirror the `ShaderConfig.cs` file. This method is faster but more likely to result in an error due to a mistake.
  * Use the Editor to generate the `ShaderConfig.cs.hlsl` file from the `ShaderConfig.cs` file, which might take longer than a manual edit but ensures that the two files are synchronized.

To use the Editor to generate the `ShaderConfig.cs.hlsl` file, follow these
steps:

  1. In the **Project** window, go to **Packages** > **Universal RP Config** > **Runtime** and open **ShaderConfig.cs**.
  2. Edit the values of the properties you want to change and then save and close the file.
  3. In the Editor, select **Edit** > **Rendering** > **Generate Shader Includes**.
  4. Unity automatically configures your project and **shaders** A program that runs on the GPU. [More info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader) to use the new configuration.

### Update the URP Config package

When you use the Package Manager to update your URP package, the Package
Manager downloads the latest version of the URP Config package to the
`/Library/PackageCache/` folder, but doesn’t automatically update the files of
the URP Config package in your `Packages` folder. Instead, you need to
manually update your copy of the URP Config package in your `Packages` folder
and reapply your changes. To do this, use the following steps:

  1. Make a copy of the `com.unity.render-pipelines.universal-config` from your `Packages` folder. You can reference this later when you reapply your changes.
  2. Delete the `com.unity.render-pipelines.universal-config` folder in your `Packages` folder.
  3. Copy the `com.unity.render-pipelines.universal-config` folder again from the `/Library/PackageCache/` folder to your `Packages` folder, as shown above in the Set up the URP Config package section.
  4. Manually reapply your modifications to the updated copy of the URP Config package.

[](../urp/quality/change-urp-asset-settings.html)

Change URP Asset settings at runtime

[](../urp/anti-aliasing.html)

Add anti-aliasing in the Universal Render Pipeline

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

