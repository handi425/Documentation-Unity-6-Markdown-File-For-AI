[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-asset-packs-manage.html)
  * [中文](/cn/current/Manual/android-asset-packs-manage.html)
  * [日本語](/ja/current/Manual/android-asset-packs-manage.html)
  * [한국어](/kr/current/Manual/android-asset-packs-manage.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-asset-packs-manage.html)
  * [中文](/cn/current/Manual/android-asset-packs-manage.html)
  * [日本語](/ja/current/Manual/android-asset-packs-manage.html)
  * [한국어](/kr/current/Manual/android-asset-packs-manage.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Developing for Android](android-developing.html)
  * [Android application size restrictions](android-application-size-restrictions.html)
  * [Play Asset Delivery](play-asset-delivery.html)
  * Manage asset packs at runtime

[](android-asset-packs-create-custom.html)

Create a custom asset pack

[](android-graphics.html)

Graphics for Android

# Manage asset packs at runtime

Unity provides [APIs](../ScriptReference/Android.AndroidAssetPacks.html) to
manage asset packs at runtime. They use Google’s PlayCore API, which means
they have the same limitations as PlayCore, and can’t manage `install-time`
asset packs. Using the PlayCore API also means your application requires the
[PlayCore](https://developer.android.com/guide/playcore) **plug-in** A set of
code created outside of Unity that creates functionality in Unity. There are
two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET
assemblies created with tools like Visual Studio) and Native plug-ins
(platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in). If your project has asset packs,
either custom asset packs or Unity-generated asset packs, Unity automatically
adds the PlayCore dependency to the application’s manifest.

The way you download asset packs and access their assets depends on the asset
pack delivery mode. There are three asset pack delivery modes:

  * `install-time`: Google Play automatically downloads `install-time` asset packs when the device installs the application. Google Play considers these asset packs to be part of the base application, and an end user can’t uninstall them without uninstalling the entire application. The PlayCore API doesn’t handle `install-time` asset packs, which means that you can’t check the status, request to download, or remove `install-time` asset packs. You also can’t directly access assets inside of these asset packs, except streaming assets in Unity-generated `install-time` asset packs. To access streaming assets, use [Application.streamingAssetsPath](../ScriptReference/Application-streamingAssetsPath.html) to get the path to streaming assets location, then use [UnityWebRequest](../ScriptReference/Networking.UnityWebRequest.html) to access assets in that path. If you create a custom asset pack, you can’t access assets inside it using standard file APIs. Instead, use [Android’s AssetManager APIs](https://developer.android.com/guide/playcore/asset-delivery/integrate-java#install-time-delivery).
  * `fast-follow`: Google Play automatically starts to download `fast-follow` asset packs after it installs the application. However, it’s possible that not all `fast-follow` asset packs are available on the first time the application launches. To check the status and download `fast-follow` asset packs, refer to Download asset packs.
  * `on-demand`: Google Play doesn’t automatically download `on-demand` asset packs. You have to manually start the download. For information on how to do this, refer to Download asset packs.

For more information about delivery modes, refer to [Delivery
modes](https://developer.android.com/guide/playcore/asset-delivery#delivery-
modes).

## Download asset packs

If your application uses `fast-follow` or `on-demand` asset packs, the device
must download these asset packs before the application can access assets
inside of them. To check the status of asset packs and download them if
they’re not on the device, you must first know the name of each asset pack. To
get the names of Unity-generated asset packs, call
[AndroidAssetPacks.GetCoreUnityAssetPackNames](../ScriptReference/Android.AndroidAssetPacks.GetCoreUnityAssetPackNames.html).
There is no runtime API to get the names of [custom asset packs](android-
asset-packs-in-unity.html#custom-asset-packs) so you must keep track of them
yourself. You set the name of custom asset packs at build time; it’s the name
of the directory.

After you have the names of your asset packs, to check the status of each
asset pack, call
[AndroidAssetPacks.GetAssetPackStateAsync](../ScriptReference/Android.AndroidAssetPacks.GetAssetPackStateAsync.html),
passing in the asset pack name. This returns the status of the asset pack you
query, and you can use the result to determine whether you need to download
the asset pack. If you want to quickly query the status of every Unity-
generated asset pack, you can use
[AndroidAssetPacks.coreUnityAssetPacksDownloaded](../ScriptReference/Android.AndroidAssetPacks-
coreUnityAssetPacksDownloaded.html). This helps you to ensure that every
Unity-generated asset pack is available before you load any **scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) other than the first one or try to
access other resources that Unity handles.

For every asset pack you need to download, call
[AndroidAssetPacks.DownloadAssetPackAsync](../ScriptReference/Android.AndroidAssetPacks.DownloadAssetPackAsync.html),
passing in the asset pack name. While the asset pack downloads, monitor the
download status because downloads can pause or fail. There are two ways to do
this:

  * Periodically check the [DownloadAssetPackAsyncOperation](../ScriptReference/Android.DownloadAssetPackAsyncOperation.html) instance that AndroidAssetPacks.DownloadAssetPackAsync returns.
  * Use the version of [AndroidAssetPacks.DownloadAssetPackAsync](../ScriptReference/Android.AndroidAssetPacks.DownloadAssetPackAsync.html) that takes a callback as its second parameter. The callback you pass in must take an [AndroidAssetPackInfo](../ScriptReference/Android.AndroidAssetPackInfo.html) as a parameter that you can use to determine the state of the download.

## Additional resources

  * [Asset packs in Unity](android-asset-packs-in-unity.html)

[](android-asset-packs-create-custom.html)

Create a custom asset pack

[](android-graphics.html)

Graphics for Android

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

