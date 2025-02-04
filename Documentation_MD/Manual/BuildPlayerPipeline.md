[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/BuildPlayerPipeline.html)
  * [中文](/cn/current/Manual/BuildPlayerPipeline.html)
  * [日本語](/ja/current/Manual/BuildPlayerPipeline.html)
  * [한국어](/kr/current/Manual/BuildPlayerPipeline.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/BuildPlayerPipeline.html)
  * [中文](/cn/current/Manual/BuildPlayerPipeline.html)
  * [日本語](/ja/current/Manual/BuildPlayerPipeline.html)
  * [한국어](/kr/current/Manual/BuildPlayerPipeline.html)

  * [Platform development ](PlatformSpecific.html)
  * [Cross-platform features and considerations](cross-platform-features.html)
  * Build Player Pipeline

[](ReducingFilesize.html)

Reducing the file size of your build

[](mobile-accessibility.html)

Accessibility for mobile applications

# Build Player Pipeline

When building a player, you sometimes want to modify the built player in some
way. For example you might want to add a custom icon, copy some documentation
next to the player or build an Installer. You can do this via editor scripting
using
[BuildPipeline.BuildPlayer](../ScriptReference/BuildPipeline.BuildPlayer.html)
to run the build and then follow it with whatever postprocessing code you
need:

    
    
    // C# example.
    using UnityEditor;
    using System.Diagnostics;
    
    public class ScriptBatch 
    {
        [MenuItem("MyTools/Windows Build With Postprocess")]
        public static void BuildGame ()
        {
            // Get filename.
            string path = EditorUtility.SaveFolderPanel("Choose Location of Built Game", "", "");
            string[] levels = new string[] {"Assets/Scene1.unity", "Assets/Scene2.unity"};
    
            // Build player.
            BuildPipeline.BuildPlayer(levels, path + "/BuiltGame.exe", BuildTarget.StandaloneWindows, BuildOptions.None);
    
            // Copy a file from the project folder to the build folder, alongside the built game.
            FileUtil.CopyFileOrDirectory("Assets/Templates/Readme.txt", path + "Readme.txt");
    
            // Run the game (Process class from System.Diagnostics).
            Process proc = new Process();
            proc.StartInfo.FileName = path + "/BuiltGame.exe";
            proc.Start();
        }
    }
    
    

## PostProcessBuild Attribute

You can also use the postprocessOrder parameter of the
[PostProcessBuildAttribute](../ScriptReference/Callbacks.PostProcessBuildAttribute.html)
to define the execution order for your build methods, and call your external
**scripts** A piece of code that allows you to create your own Components,
trigger game events, modify Component properties over time and respond to user
input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) with the Process class from these
methods as shown in the last section. This parameter is used to sort the build
methods from lower to higher, and you can assign any negative or positive
value to it.

[](ReducingFilesize.html)

Reducing the file size of your build

[](mobile-accessibility.html)

Accessibility for mobile applications

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

