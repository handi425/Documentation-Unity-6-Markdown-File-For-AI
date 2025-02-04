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

# EditorUserBuildSettings

class in UnityEditor

/

Inherits from:[Object](Object.html)

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

User build settings for the Editor

Additional resources: [EditorBuildSettings](EditorBuildSettings.html).

### Static Properties

[activeBuildTarget](EditorUserBuildSettings-activeBuildTarget.html)| The
currently active build target.  
---|---  
[activeScriptCompilationDefines](EditorUserBuildSettings-
activeScriptCompilationDefines.html)| DEFINE directives for the compiler.  
[allowDebugging](EditorUserBuildSettings-allowDebugging.html)| Enable source-
level debuggers to connect.  
[androidBuildSubtarget](EditorUserBuildSettings-androidBuildSubtarget.html)|
Android platform options.  
[buildAppBundle](EditorUserBuildSettings-buildAppBundle.html)| Set to true to
build an Android App Bundle (aab file) instead of an apk. The default value is
false.  
[buildScriptsOnly](EditorUserBuildSettings-buildScriptsOnly.html)| Is build
script only enabled.  
[buildWithDeepProfilingSupport](EditorUserBuildSettings-
buildWithDeepProfilingSupport.html)| Enables Deep Profiling support in the
Player.  
[compressFilesInPackage](EditorUserBuildSettings-compressFilesInPackage.html)|
Compress files in package.  
[connectProfiler](EditorUserBuildSettings-connectProfiler.html)| Start the
player with a connection to the profiler.  
[development](EditorUserBuildSettings-development.html)| Enables a development
build.  
[explicitArrayBoundsChecks](EditorUserBuildSettings-
explicitArrayBoundsChecks.html)| Are array bounds actively validated?  
[explicitDivideByZeroChecks](EditorUserBuildSettings-
explicitDivideByZeroChecks.html)| Are divide by zero's actively validated?  
[explicitNullChecks](EditorUserBuildSettings-explicitNullChecks.html)| Are
null references actively validated?  
[exportAsGoogleAndroidProject](EditorUserBuildSettings-
exportAsGoogleAndroidProject.html)| Export Android Project for use with
Android Studio/Gradle.  
[forceInstallation](EditorUserBuildSettings-forceInstallation.html)| Force
installation of package, even if error.  
[installInBuildFolder](EditorUserBuildSettings-installInBuildFolder.html)|
Place the built player in the build folder.  
[iOSXcodeBuildConfig](EditorUserBuildSettings-iOSXcodeBuildConfig.html)| The
scheme Xcode uses to run this project.  
[macOSXcodeBuildConfig](EditorUserBuildSettings-macOSXcodeBuildConfig.html)|
The scheme Xcode uses to run this project.  
[managedDebuggerFixedPort](EditorUserBuildSettings-
managedDebuggerFixedPort.html)| Force the port used by the managed debugger.
Default is 0 which means platform-specific auto-selection of a port.  
[movePackageToDiscOuterEdge](EditorUserBuildSettings-
movePackageToDiscOuterEdge.html)| Places the package on the outer edge of the
disk.  
[needSubmissionMaterials](EditorUserBuildSettings-
needSubmissionMaterials.html)| Build submission materials.  
[overrideMaxTextureSize](EditorUserBuildSettings-overrideMaxTextureSize.html)|
The override for the maximum texture size when importing assets.  
[overrideTextureCompression](EditorUserBuildSettings-
overrideTextureCompression.html)| The asset importing override of texture
compression.  
[selectedBuildTargetGroup](EditorUserBuildSettings-
selectedBuildTargetGroup.html)| The currently selected build target group.  
[selectedStandaloneTarget](EditorUserBuildSettings-
selectedStandaloneTarget.html)| The currently selected target for a standalone
build.  
[standaloneBuildSubtarget](EditorUserBuildSettings-
standaloneBuildSubtarget.html)| Desktop standalone build subtarget.  
[symlinkSources](EditorUserBuildSettings-symlinkSources.html)| Symlink sources
when generating the project.  
[waitForManagedDebugger](EditorUserBuildSettings-waitForManagedDebugger.html)|
Instructs the player to wait for managed debugger to attach before executing
any script code.  
[waitForPlayerConnection](EditorUserBuildSettings-
waitForPlayerConnection.html)| Sets the Player to wait for player connection
on player start.  
[webGLBuildSubtarget](EditorUserBuildSettings-webGLBuildSubtarget.html)| WebGL
Build subtarget.  
[webGLClientBrowserPath](EditorUserBuildSettings-webGLClientBrowserPath.html)|
The path to the executable of the browser in which to load the web
application.  
[webGLClientBrowserType](EditorUserBuildSettings-webGLClientBrowserType.html)|
Defines the client browser type in which to load the web application.  
[windowsBuildAndRunDeployTarget](EditorUserBuildSettings-
windowsBuildAndRunDeployTarget.html)| Sets and gets the Windows device to
launch the Windows app when using Build and Run.  
[windowsDevicePortalAddress](EditorUserBuildSettings-
windowsDevicePortalAddress.html)| Specifies the Windows DevicePortal
connection address of the device to deploy and launch the UWP app on when
using Build and Run.  
[windowsDevicePortalPassword](EditorUserBuildSettings-
windowsDevicePortalPassword.html)| Specifies the Windows DevicePortal password
for the device to deploy and launch the UWP app on when using Build and Run.  
[windowsDevicePortalUsername](EditorUserBuildSettings-
windowsDevicePortalUsername.html)| Specifies the Windows DevicePortal username
for the device to deploy and launch the UWP app on when using Build and Run.  
[wsaBuildAndRunDeployTarget](EditorUserBuildSettings-
wsaBuildAndRunDeployTarget.html)| Sets and gets the Windows device to launch
the UWP app when using Build and Run.  
[wsaUWPBuildType](EditorUserBuildSettings-wsaUWPBuildType.html)| The build
type for the Universal Windows Platform.  
[wsaUWPSDK](EditorUserBuildSettings-wsaUWPSDK.html)| Sets and gets target UWP
SDK to build Windows Store application against.  
[wsaUWPVisualStudioVersion](EditorUserBuildSettings-
wsaUWPVisualStudioVersion.html)| Sets and gets Visual Studio version to build
Windows Store application with.  
  
### Static Methods

[GetBuildLocation](EditorUserBuildSettings.GetBuildLocation.html)| Returns the
location used for the last saved build.  
---|---  
[SetBuildLocation](EditorUserBuildSettings.SetBuildLocation.html)| Set a new
location for the build.  
[SwitchActiveBuildTarget](EditorUserBuildSettings.SwitchActiveBuildTarget.html)|
Select a new build target to be active.  
[SwitchActiveBuildTargetAsync](EditorUserBuildSettings.SwitchActiveBuildTargetAsync.html)|
Select a new build target to be active during the next Editor update.  
  
### Inherited Members

### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
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

