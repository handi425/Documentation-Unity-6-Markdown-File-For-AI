[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/uwp-package-app-vs.html)
  * [中文](/cn/current/Manual/uwp-package-app-vs.html)
  * [日本語](/ja/current/Manual/uwp-package-app-vs.html)
  * [한국어](/kr/current/Manual/uwp-package-app-vs.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/uwp-package-app-vs.html)
  * [中文](/cn/current/Manual/uwp-package-app-vs.html)
  * [日本語](/ja/current/Manual/uwp-package-app-vs.html)
  * [한국어](/kr/current/Manual/uwp-package-app-vs.html)

  * [Platform development ](PlatformSpecific.html)
  * [Universal Windows Platform](WindowsStore.html)
  * [Build and deliver for Universal Windows Platform](uwp-building-and-delivering.html)
  * Package a UWP app in Visual Studio

[](windowsstore-generatedproject-il2cpp.html)

Generate your Visual Studio C++ solution

[](windowsstore-deployment.html)

Deploy a UWP application

# Package a UWP app in Visual Studio

Before you distribute your Universal Windows Platform (UWP) application, you
need to package it in Visual Studio. For more information, refer to Microsoft
documentation on [packaging a desktop or UWP app in Visual
Studio](https://learn.microsoft.com/en-us/windows/msix/package/packaging-uwp-
apps).

## Create an app package in Visual Studio

To create an app package in Visual Studio:

  1. Open your built UWP project in Visual Studio.
  2. In the **Solution Explorer** , right-click on your main project.
  3. Go to **Publish** > **Create App Packages**. The **Create App Packages** wizard appears.
  4. Select **Microsoft Store using a new app name** and then click **Next**.   
**Note:** If you choose **Sideloading** , Visual Studio will not generate the
app package upload file for Partner Center submissions. You can select the
**Sideloading** option if you only want to create a MSIX package for non-Store
distribution.

  5. On the next page, sign in to the Partner Center with your developer account. If you don’t have a developer account yet, the wizard will show you how to create one.
  6. Select the app name for your package from the list of apps currently registered to your account, or reserve a new name in the Partner Center.
  7. In the **Select and Configure Packages** dialog, select the architectures you want to target based on the devices you want to deploy your application to.
  8. In the **Generate app bundle** listbox, select **Always**.
  9. Click **Create** to generate the app package.

Your app is now successfully packaged.

## Install your package on your machine

After you create your app package, use the following steps to install the
package on your machine:

  1. Open the folder which contains your package.
  2. Right-click on the `Add-AppxPackage <yourappx>.appx` file. Choose **Run with PowerShell** and follow the prompts.
  3. If you [signed your file](https://learn.microsoft.com/en-us/windows/msix/package/sign-app-package-using-signtool), the file will now install on your machine.  
**Note:** If you’re re-installing an .appx file, you must uninstall the file
that was previously installed by right-clicking the file icon, and then
clicking **Uninstall**.

[](windowsstore-generatedproject-il2cpp.html)

Generate your Visual Studio C++ solution

[](windowsstore-deployment.html)

Deploy a UWP application

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

