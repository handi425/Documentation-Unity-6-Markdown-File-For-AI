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

# BuildOptions

enumeration

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

### Description

Building options. Multiple options can be combined together.

Additional resources:
[BuildPipeline.BuildPlayer](BuildPipeline.BuildPlayer.html).

### Properties

[None](BuildOptions.None.html)| Perform the specified build without any
special settings or extra tasks.  
---|---  
[Development](BuildOptions.Development.html)| Build a development version of
the player.  
[AutoRunPlayer](BuildOptions.AutoRunPlayer.html)| Run the built player.  
[ShowBuiltPlayer](BuildOptions.ShowBuiltPlayer.html)| Show the built player.  
[BuildAdditionalStreamedScenes](BuildOptions.BuildAdditionalStreamedScenes.html)|
For internal use  
[AcceptExternalModificationsToPlayer](BuildOptions.AcceptExternalModificationsToPlayer.html)|
Used when building Xcode (iOS) or Eclipse (Android) projects.  
[CleanBuildCache](BuildOptions.CleanBuildCache.html)| Clear all cached build
results, resulting in a full rebuild of all scripts and all player data.  
[ConnectWithProfiler](BuildOptions.ConnectWithProfiler.html)| Start the player
with a connection to the profiler in the editor.  
[AllowDebugging](BuildOptions.AllowDebugging.html)| Allow script debuggers to
attach to the Player remotely. You can debug your scripts only if you use
BuildOptions.Development.  
[SymlinkSources](BuildOptions.SymlinkSources.html)| Symlink sources when
generating the project. This is useful if you're changing source files inside
the generated project and want to bring the changes back into your Unity
project or a package.  
[UncompressedAssetBundle](BuildOptions.UncompressedAssetBundle.html)| Don't
compress the data when creating the asset bundle.  
[ConnectToHost](BuildOptions.ConnectToHost.html)| Sets the Player to connect
to the Editor.  
[CustomConnectionID](BuildOptions.CustomConnectionID.html)| Determines if the
player should be using the custom connection ID.  
[BuildScriptsOnly](BuildOptions.BuildScriptsOnly.html)| Only build the scripts
in a Project.  
[PatchPackage](BuildOptions.PatchPackage.html)| Patch a Development app
package rather than completely rebuilding it.Supported platforms: Android.  
[ForceEnableAssertions](BuildOptions.ForceEnableAssertions.html)| Include
assertions in the build. By default, the assertions are only included in
development builds.  
[CompressWithLz4](BuildOptions.CompressWithLz4.html)| Use chunk-based LZ4
compression when building the Player.  
[CompressWithLz4HC](BuildOptions.CompressWithLz4HC.html)| Use chunk-based LZ4
high-compression when building the Player.  
[StrictMode](BuildOptions.StrictMode.html)| Do not allow the build to succeed
if any errors are reporting during it.  
[IncludeTestAssemblies](BuildOptions.IncludeTestAssemblies.html)| Build will
include Assemblies for testing.  
[NoUniqueIdentifier](BuildOptions.NoUniqueIdentifier.html)| Will force the
buildGUID to all zeros.  
[WaitForPlayerConnection](BuildOptions.WaitForPlayerConnection.html)| Sets the
Player to wait for player connection on player start.  
[EnableCodeCoverage](BuildOptions.EnableCodeCoverage.html)| Enables code
coverage. You can use this as a complimentary way of enabling code coverage on
platforms that do not support command line arguments.  
[EnableDeepProfilingSupport](BuildOptions.EnableDeepProfilingSupport.html)|
Enables Deep Profiling support in the player.  
[DetailedBuildReport](BuildOptions.DetailedBuildReport.html)| Generates more
information in the BuildReport.  
  
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

