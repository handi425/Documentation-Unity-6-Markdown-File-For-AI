[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/allow-deny-vulkan-usage.html)
  * [中文](/cn/current/Manual/allow-deny-vulkan-usage.html)
  * [日本語](/ja/current/Manual/allow-deny-vulkan-usage.html)
  * [한국어](/kr/current/Manual/allow-deny-vulkan-usage.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/allow-deny-vulkan-usage.html)
  * [中文](/cn/current/Manual/allow-deny-vulkan-usage.html)
  * [日本語](/ja/current/Manual/allow-deny-vulkan-usage.html)
  * [한국어](/kr/current/Manual/allow-deny-vulkan-usage.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Developing for Android](android-developing.html)
  * [Graphics for Android](android-graphics.html)
  * Allow or deny Vulkan API usage

[](vulkan-swapchain-pre-rotation.html)

Framebuffer orientation

[](android-testing-and-debugging.html)

Testing and debugging

# Allow or deny Vulkan API usage

By default, Unity prevents Android devices known to run Unity applications
sub-optimally with Vulkan graphics API. However, your testing might reveal
that some restricted devices actually run your application better with Vulkan
API than with OpenGLES3 API. Alternatively, you might want to further restrict
some devices to run your application with Vulkan API. Using **Android Vulkan
Allow and Deny Filter Lists** , you can fine tune which devices you want to
allow to run your application with Vulkan API.

With **Android Vulkan Allow Filter List** , you can allow certain devices to
use Vulkan as the default graphics API to run your application. Alternatively,
with **Android Vulkan Deny Filter List** , you can limit certain devices from
using Vulkan API to run your application. For both types of list, you can
specify values for the following parameters to identify a device or set of
devices:

  * Vendor
  * Device Name
  * Brand
  * Product Name
  * Android OS version
  * Vulkan API version
  * Driver version

You can use C# regular expressions for all the parameters, except Vulkan API
version and Driver version. For example, `[A|a]dreno .*6[0-9][0-9]`, `Qual*`,
`[S|s]amsung`. The Unity Editor displays an error for an invalid regular
expression.

The device properties must match all the parameter values (logical AND) to
determine whether it’s allowed or denied to run your application with Vulkan
API. The Allow Filter List identifies all the devices with Vulkan API and
driver versions equal to or greater than the specified parameter values. For
example, if you specify the GPU vendor as Qualcomm, the GPU model name as
Adreno, and Vulkan API version as `1.1.128`, the Allow Filter List will allow
all the devices with Qualcomm Adreno GPU that have Vulkan API version greater
than or equal to `1.1.128`.

The Deny Filter List identifies all the devices with Vulkan API and driver
versions less than or equal to the specified parameter values. For example, if
you specify the GPU vendor as ARM, the GPU model name as Mali, and Vulkan
driver version as `0.676.0`, the Deny Filter List will restrict all the
devices with ARM Mali GPU that have Vulkan driver version less than or equal
to `0.676.0`.

**Note** : Although you can restrict the use of Vulkan on a group of devices,
you can use the Allow Filter List to enable particular devices from that group
to still use Vulkan.

To allow Android devices to always use Vulkan API, use the following steps:

  1. From the main menu, navigate to **Edit** > **Project Settings** > **Player** > **Android settings** > **Other Settings**.
  2. In the **Vulkan Settings** section, go to **Android Vulkan Allow Filter List** and use the foldout (triangle) to expand it.
  3. Select the **Add** (+) button to add specifications of the Android device that you want to allow the Vulkan API usage on. A set of parameters is displayed.
  4. Enter the device specifications in the available parameters. All the parameters are optional. For the description of parameters, refer to [Android Player settings](class-PlayerSettingsAndroid.html#DenyFilterList).

Android devices that meet the specifications defined in the parameter values
will always use Vulkan API for Unity applications.

To restrict Android devices from using Vulkan API, use **Android Vulkan Deny
Filter List** and follow the same steps as earlier.

**Notes** :

  * If you set same values in both Allow and Deny Filter Lists, Unity ignores the criteria defined by those values.
  * The restricted devices use a fallback graphics API set in the **Player settings** Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings) to run your application. If no
fallback API is available, the application won’t launch.

  * You can also use [androidVulkanDenyFilterList](../ScriptReference/PlayerSettings.Android-androidVulkanDenyFilterList.html) and [androidVulkanAllowFilterList](../ScriptReference/PlayerSettings.Android-androidVulkanAllowFilterList.html) APIs to allow or restrict the use of Vulkan API on Android devices.

## Additional resources

  * [Regular expressions](https://learn.microsoft.com/en-us/dotnet/standard/base-types/regular-expressions)

[](vulkan-swapchain-pre-rotation.html)

Framebuffer orientation

[](android-testing-and-debugging.html)

Testing and debugging

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

