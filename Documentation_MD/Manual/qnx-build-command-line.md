[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/qnx-build-command-line.html)
  * [中文](/cn/current/Manual/qnx-build-command-line.html)
  * [日本語](/ja/current/Manual/qnx-build-command-line.html)
  * [한국어](/kr/current/Manual/qnx-build-command-line.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/qnx-build-command-line.html)
  * [中文](/cn/current/Manual/qnx-build-command-line.html)
  * [日本語](/ja/current/Manual/qnx-build-command-line.html)
  * [한국어](/kr/current/Manual/qnx-build-command-line.html)

  * [Platform development ](PlatformSpecific.html)
  * [Embedded systems](embedded-systems.html)
  * [QNX](qnx.html)
  * [Build and deliver for QNX](qnx-build-and-deliver.html)
  * Build for QNX from the command line

[](qnx-build-settings.html)

QNX Build Profiles reference

[](qnx-deploy.html)

Deploy a QNX project

# Build for QNX from the command line

To build a Unity project for the QNX system on the command line interface
(CLI), you must have the Unity Editor installed on the build host. The build
host must be running a Linux operating system and also have the QNX SDK
installed. For more information, refer to [Install the Unity Editor for
QNX](qnx-install-editor.html).

The following example uses the Linux variant of the executable (`Unity`), but
you can replace it with an equivalent executable for your preferred build
host’s operating system.

## Command line arguments

**Prerequisites**

Make sure you’ve followed these instructions before building the project using
the command line:

  * Set up `QNX_TARGET` and `QNX_HOST` as per [Install the Unity Editor for QNX](qnx-install-editor.html).

To instruct Unity to start in CLI mode and build the project at `<path-to-
unity-project-root>` for QNX, run the following command:

    
    
    Unity -quit -batchmode -nographics -buildTarget QNX -executeMethod Builder.Build -projectPath <path-to-unity-project-root>
    

The build process also calls the function `Builder.Build` to continue with the
build setup.

## Build script

You can add the example build script into `Assets/Editor/` for the project to
you’re building from the command line. Use the `-executeMethod` option to call
the `Build()` method of this class, which sets up the build options and
triggers the build.

For more information, refer to the `BuildPipeline.BuildPlayer`
[documentation](../ScriptReference/BuildPipeline.BuildPlayer.html).

    
    
    using UnityEditor;
    using UnityEditor.Build.Reporting;
    using UnityEngine;
    
    public class Builder
    {
        private static void BuildQNX(QNXOsVersion qnxVersion, QNXArchitecture architecture)
        {
            // Set QNX version in BuildSettings
            EditorUserBuildSettings.selectedQnxOsVersion = qnxVersion;
    
            // Set architecture in BuildSettings
            EditorUserBuildSettings.selectedQnxArchitecture = architecture;
    
            // Setup build options (e.g. scenes, build output location)
            var options = new BuildPlayerOptions
            {
                // Change to scenes from your project
                scenes = new[]
                {
                    "Assets/Scenes/SampleScene.unity",
                },
                // Change to location the output should go
                locationPathName = "../QNXPlayer/",
                options = BuildOptions.CleanBuildCache | BuildOptions.StrictMode,
                target = BuildTarget.QNX
            };
    
            var report = BuildPipeline.BuildPlayer(options);
    
            if (report.summary.result == BuildResult.Succeeded)
            {
                Debug.Log($"Build successful - Build written to {options.locationPathName}");
            }
            else if (report.summary.result == BuildResult.Failed)
            {
                Debug.LogError($"Build failed");
            }
        }
    
        // This function will be called from the build process
        public static void Build()
        {
            // Build QNX 7.1 ARM64 Unity player
            BuildQNX(QNXOsVersion.Neutrino71, QNXArchitecture.Arm64);
        }
    }
    

## Additional resources

  * [Install the Unity Editor for QNX](qnx-install-editor.html)
  * [QNX Build Profiles reference](qnx-build-settings.html)

[](qnx-build-settings.html)

QNX Build Profiles reference

[](qnx-deploy.html)

Deploy a QNX project

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

