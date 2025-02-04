[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/iphone-playerSizeOptimization.html)
  * [中文](/cn/current/Manual/iphone-playerSizeOptimization.html)
  * [日本語](/ja/current/Manual/iphone-playerSizeOptimization.html)
  * [한국어](/kr/current/Manual/iphone-playerSizeOptimization.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/iphone-playerSizeOptimization.html)
  * [中文](/cn/current/Manual/iphone-playerSizeOptimization.html)
  * [日本語](/ja/current/Manual/iphone-playerSizeOptimization.html)
  * [한국어](/kr/current/Manual/iphone-playerSizeOptimization.html)

  * [Platform development ](PlatformSpecific.html)
  * [iOS](iphone.html)
  * [Developing for iOS](ios-developing.html)
  * [Optimize performance for iOS](iphone-performance.html)
  * Optimize the size of the iOS Player

[](iphone-InternalProfiler.html)

Measure performance with the built-in profiler

[](PluginsForIOS.html)

Native plug-ins for iOS

# Optimize the size of the iOS Player

There are two main ways to reduce the size of the built iOS Player: create a
Release build within Xcode, or change the Stripping Level within Unity.

## Release build

It’s recommended to create final release builds within Xcode. Navigate to the
menu bar and select **Product** > **Archive**. This option ensures the build
has the correct release configuration and strips any debug symbols. After
issuing this command, Xcode switches to the Organizer window Archives tab. For
further information on how to calculate app size, and for other size-reducing
tips, refer to [Reducing the size of my
App](https://developer.apple.com/library/content/qa/qa1795/_index.html).

**Note** : It’s recommended to factor in a small margin for error when aiming
for the over-the-air download limit. The current download limit is set at
200MB. However, starting with iOS 13, the app users have the option to
override this limit to download apps larger than 200MB.

## Managed code stripping

Unity removes unused or unreachable code during the build process through a
technique called managed code stripping, which can significantly reduce the
final size of your application. Refer to [managed code stripping](managed-
code-stripping.html) for more information.

**Note:** It can sometimes be difficult to determine which classes are getting
stripped in error, even though the application requires them. You can often
get useful information about this by running the stripped application on the
[simulator](https://developer.apple.com/documentation/xcode/running-your-app-
in-simulator-or-on-a-device) and checking the Xcode console for error
messages.

## Reduce the build size

Use the following checklist to help reduce the size of your build:

  * Enable **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](class-TextureImporterOverride), [Animation Compression](class-AnimationClip.html#AssetProperties), [Audio Compression](class-AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) for textures and minimize the
number of uncompressed sounds. For more information, and tips on file size
reduction, refer to [Reducing the file size of your
build](ReducingFilesize.html).

  * From the [**iOS Player settings**](class-PlayerSettingsiOS.html) window: 
    * Enable [**Strip Engine Code**](class-PlayerSettingsiOS.html#Optimization)
    * Set the script call optimization level to [**Fast but no exceptions**](class-PlayerSettingsiOS.html#Optimization)
    * Set the API Compatibility Level to [**.Net Standard**](class-PlayerSettingsiOS.html#Configuration)
  * Remove unnecessary code dependencies.
  * Avoid generic containers in combination with value types, including structs.

## Minimum Unity application size

If disabling size optimizations, it’s expected that an empty project might be
around 20MB in the App Store. Using code stripping, an application containing
an empty **scene** A Scene contains the environments and menus of your game.
Think of each unique Scene file as a unique level. In each Scene, you place
your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) can be reduced to less than 12MB in the
App Store. However, the application must be zipped and have digital rights
management (DRM) attached.

## Increased application size in the Apple App Store

When publishing your app, Apple App Store service first encrypts the binary
file and then compresses it via zip. Encryption increases the randomness of
the code segment, and can increase the applications size before compression.

[](iphone-InternalProfiler.html)

Measure performance with the built-in profiler

[](PluginsForIOS.html)

Native plug-ins for iOS

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

