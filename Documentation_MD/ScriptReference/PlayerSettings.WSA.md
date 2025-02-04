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

# WSA

class in UnityEditor

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

[Switch to Manual](../Manual/class-PlayerSettings.html "Go to PlayerSettings
Component in the Manual")

### Description

Provides access to Microsoft Store App-specific player settings.

You can use these properties and methods to programmatically access [Universal
Windows Platform-specific build settings](../Manual/class-
PlayerSettingsWSA.html#Publishing.html).

### Static Properties

[applicationDescription](PlayerSettings.WSA-applicationDescription.html)| The
description text that the Microsoft Store displays with your application.  
---|---  
[certificateIssuer](PlayerSettings.WSA-certificateIssuer.html)| The
certificate issuer for the current Universal Windows Platform certificate.  
[certificateNotAfter](PlayerSettings.WSA-certificateNotAfter.html)| The
expiration date for the current Universal Windows Platform certificate.  
[certificatePath](PlayerSettings.WSA-certificatePath.html)| The file path for
the current Universal Windows Platform certificate.  
[certificateSubject](PlayerSettings.WSA-certificateSubject.html)| The subject
for the current Universal Windows Platform certificate.  
[defaultTileSize](PlayerSettings.WSA-defaultTileSize.html)| The tile size type
to use as the default size for the application's tile.  
[inputSource](PlayerSettings.WSA-inputSource.html)| The input source type for
mouse, pen, and touch input events in a XAML app.  
[largeTileShowName](PlayerSettings.WSA-largeTileShowName.html)| The
application name to display on the Large Tile.  
[lastRequiredScene](PlayerSettings.WSA-lastRequiredScene.html)| The scene
index number from the Scenes in Build list for the last scene that must be
present in a Streaming Install build.  
[mediumTileShowName](PlayerSettings.WSA-mediumTileShowName.html)| The
application name to display on the Medium Tile.  
[packageName](PlayerSettings.WSA-packageName.html)| The name of the Universal
Windows Platform application package to install on the device.  
[packageVersion](PlayerSettings.WSA-packageVersion.html)| The version of the
Universal Windows Platform application package to install on the device.  
[splashScreenBackgroundColor](PlayerSettings.WSA-
splashScreenBackgroundColor.html)| The Override background color for the Unity
splash screen.  
[supportStreamingInstall](PlayerSettings.WSA-supportStreamingInstall.html)|
Indicates whether you can launch the Universal Windows Platform application
package before installation is complete.  
[syncCapabilities](PlayerSettings.WSA-syncCapabilities.html)| Sync the
Capabilities set in the Unity Editor to the AppXManifest  
[tileBackgroundColor](PlayerSettings.WSA-tileBackgroundColor.html)| The
background color to use the application's tiles.  
[tileForegroundText](PlayerSettings.WSA-tileForegroundText.html)| The color
style to use for the title text within the application's tile.  
[tileShortName](PlayerSettings.WSA-tileShortName.html)| An alternative,
shorter title name to display in the application's tile.  
[tileShowName](PlayerSettings.WSA-tileShowName.html)| Indicates which tiles
display the application's display name.  
[transparentSwapchain](PlayerSettings.WSA-transparentSwapchain.html)| Sets
AlphaMode on the swap chain to DXGI_ALPHA_MODE_PREMULTIPLIED.  
[vcxProjDefaultLanguage](PlayerSettings.WSA-vcxProjDefaultLanguage.html)| Sets
the XML <defaultLanguage> value specified in the generated Visual Studio
project file (.vcxproj). Applies only to the initial file generation,
preexisting files will not be modified. When empty 'en-US' will be used.Only
applies to the UWP platform.  
[wideTileShowName](PlayerSettings.WSA-wideTileShowName.html)| Indicates
whether to display the application name on the wide tile.  
  
### Static Methods

[GetCapability](PlayerSettings.WSA.GetCapability.html)| Checks if the your
project sets the specified UWP Capability.  
---|---  
[GetTargetDeviceFamily](PlayerSettings.WSA.GetTargetDeviceFamily.html)| Checks
if your project targets the specified device family.  
[GetVisualAssetsImage](PlayerSettings.WSA.GetVisualAssetsImage.html)|
Retrieves the Asset path for the image you set as the Universal Windows
Platform package logo.  
[SetCapability](PlayerSettings.WSA.SetCapability.html)| Includes or removes
the specified UWP Capability in the Universal Windows Platform build.  
[SetCertificate](PlayerSettings.WSA.SetCertificate.html)| Sets the certificate
to use to sign the Universal Windows Platform application package.  
[SetTargetDeviceFamily](PlayerSettings.WSA.SetTargetDeviceFamily.html)| Adds
or removes the specified UWP device family from the list of device families
the Universal Windows Platform application build supports.  
[SetVisualAssetsImage](PlayerSettings.WSA.SetVisualAssetsImage.html)| Sets the
image to use as the Universal Windows Platform package logo.  
  
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

