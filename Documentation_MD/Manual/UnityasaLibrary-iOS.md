[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityasaLibrary-iOS.html)
  * [中文](/cn/current/Manual/UnityasaLibrary-iOS.html)
  * [日本語](/ja/current/Manual/UnityasaLibrary-iOS.html)
  * [한국어](/kr/current/Manual/UnityasaLibrary-iOS.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityasaLibrary-iOS.html)
  * [中文](/cn/current/Manual/UnityasaLibrary-iOS.html)
  * [日本語](/ja/current/Manual/UnityasaLibrary-iOS.html)
  * [한국어](/kr/current/Manual/UnityasaLibrary-iOS.html)

  * [Platform development ](PlatformSpecific.html)
  * [iOS](iphone.html)
  * [Developing for iOS](ios-developing.html)
  * Integrating Unity into native iOS applications

[](ios-native-plugin-bonjour-sample.html)

Bonjour browser sample

[](deep-linking-ios.html)

Deep linking on iOS

# Integrating Unity into native iOS applications

This page describes how to integrate the Unity Runtime Library into iOS native
applications with the Unity as a Library feature.

You can use this feature to include Unity-powered features, such as 3D/2D
Real-Time Rendering, **AR** Augmented Reality [More info](AROverview.html)  
See in [Glossary](Glossary.html#AR) Experience, 3D model interaction, or 2D
mini-games, in your native application. The Unity Runtime Library exposes
controls to manage when and how to load, activate, and unload content in your
native application.

## How it works

To use Unity as a Library for iOS, first build your Xcode project as usual
from Unity. For more information, refer to [Build an iOS application](iphone-
BuildProcess.html).

Every Unity iOS Xcode project has the following
[structure](StructureOfXcodeProject.html):

  * A library part in the **UnityFramework** target that includes the source, **plug-ins** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in), and dependent frameworks. It also
produces a `UnityFramework.framework` file.

  * A thin launcher part in the **Unity-iPhone** target that includes app representation data and runs the library. The **Unity-iPhone** target has a single dependency on the **UnityFramework** target.

To integrate Unity into another Xcode project, you need to combine both Xcode
projects (the native one and the one Unity generates) into a single Xcode
workspace, and add the `UnityFramework.framework` file to the **Embedded
Binaries** section of the **Application** target for the native Xcode project.
Once you do this, you can use the `UnityFramework` class to control the Unity
runtime.

This [repository](https://github.com/Unity-Technologies/uaal-
example/blob/master/docs/ios.md) contains example Projects and plug-ins that
demonstrate how to integrate Unity into an Xcode project, along with further
documentation.

## UnityFramework class

You can control the Unity runtime through an instance of the `UnityFramework`
Objective-C class, which is a principal class of `UnityFramework.framework`:

**Method** | **Description**  
---|---  
`+ (UnityFramework*)getInstance;` | Singleton class method that returns an instance to `UnityFramework`.  
`- (UnityAppController*)appController;` | Returns the `UnityAppController` subclass of `UIApplicationDelegate`. This is the root Unity class on the native side, and can access the app’s View-related objects, such as `UIView`, `UIViewControllers`, `CADisplayLink`, or `DisplayConnection`.  
`- (void)setDataBundleId:(const char*)bundleId;` | Sets the Bundle where the Unity runtime should look for the _Data_ folder. For more information, see documentation on the [Data folder](StructureOfXcodeProject.html). Call this method before calling `runUIApplicationMainWithArgc` or `runEmbeddedWithArgc`.  
`- (void)runUIApplicationMainWithArgc:(int)argc argv:(char*[])argv;` | The default way to run Unity from the main method where there are no other Views.  
`- (void)runEmbeddedWithArgc:(int)argc argv:(char*[])argv appLaunchOpts:(NSDictionary*)appLaunchOpts;` | Call this method when you need to run Unity when other Views exist.  
`- (void)unloadApplication;` | Call this to unload Unity and receive a callback to `UnityFrameworkListener` after the unload completes. Unity will release most of the memory it occupies, but not all of it. You will be able to run Unity again.  
`- (void)registerFrameworkListener:(id<UnityFrameworkListener>)obj;` | Register the listener object that receives callbacks of UnityFramework lifecycle-related events.  
`- (void)unregisterFrameworkListener:(id<UnityFrameworkListener>)obj;` | Unregister a listener object.  
`- (void)showUnityWindow;` | Call this method while a non-Unity View is showing to also show a Unity View that’s already running.  
`- (void)pause:(bool)pause;` | Pause Unity.  
`- (void)setExecuteHeader:(const MachHeader*)header;` | You must call this before running Unity in order for CrashReporter to work properly.  
`- (void)sendMessageToGOWithName:(const char*)goName functionName:(const char*)name message:(const char*)msg;` | This method is a proxy to [UnitySendMessage](PluginsForIOS.html). It finds a game object by name and calls functionName with a single-string message parameter.  
`(void)quitApplication:(int)exitCode;` | Call this to unload Unity completely and receive a callback to `UnityFrameworkListener` when Unity quits. Unity will release all memory.  
  
**Note:** You won’t be able to run Unity again in the same process after this
call. You can set `quitHandler` on `AppController` to override the default
process kill.  
  
## Limitations

Unity doesn’t control the runtime lifecycle, so Unity as a Library might not
work for all possible use cases. Known limitations include:

  * Unity as a Library only supports full-screen rendering, and doesn’t support rendering on part of the screen.
  * You can’t load more than one instance of the Unity runtime.
  * You might need to adapt third-party plug-ins (both [native](plug-ins-native.html) and [managed](plug-ins-managed.html)) to work with the Unity runtime.
  * You can’t adjust the device’s status bar visibility through the [iOS Player settings](class-PlayerSettingsiOS.html#Status) when using Unity as a Library in a native iOS application. Consider using either of the following options to achieve the same: 
    * Set [`UIStatusBarHidden`](https://developer.apple.com/documentation/bundleresources/information_property_list/uistatusbarhidden?language=objc) or [`UIViewControllerBasedStatusBarAppearance`](https://developer.apple.com/documentation/bundleresources/information_property_list/uiviewcontrollerbasedstatusbarappearance?language=objc) key in the info.plist file of your project.
    * Set the view controller property [`prefersStatusBarHidden`](https://developer.apple.com/documentation/swiftui/uihostingcontroller/prefersstatusbarhidden/) and call [`setNeedsStatusBarAppearanceUpdate`](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621354-setneedsstatusbarappearanceupdat?language=objc) method.
    * Set the view controller property [`childViewControllerForStatusBarHidden`](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621451-childviewcontrollerforstatusbarh?language=objc).

* * *

  * Unity as a Library for iOS added in [2019.3](https://docs.unity3d.com/Manual/30_search.html?q=newin20193).NewIn20193

[](ios-native-plugin-bonjour-sample.html)

Bonjour browser sample

[](deep-linking-ios.html)

Deep linking on iOS

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

