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

# UnityEngine.NVIDIAModule

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

A module that contains API you can use to interact with NVIDIA graphics cards.

To activate this module at runtime, call NVIDIA.Plugins.LoadPlugin with the
NVIDIA.Plugins.Plugin.NVUnityPlugin value during application startup. The
class NVIDIA.Device contains the APIs to interact with the graphics cards'
specific features.

### Classes

[DLSSContext](NVIDIA.DLSSContext.html)| Represents the state of DLSS.  
---|---  
[GraphicsDevice](NVIDIA.GraphicsDevice.html)| Provides the main entry point
for the NVIDIA Module. Use this to interact with specific NVIDIA graphics card
features.  
[GraphicsDeviceDebugView](NVIDIA.GraphicsDeviceDebugView.html)| Represents a
memory snapshot of the current feature states. The memory of the
arrays/buffers in this struct are tied to the lifetime of the debug view.
Additional resources: GraphicsDevice.CreateDebugView,
GraphicsDevice.UpdateDebugView and GraphicsDevice.DeleteDebugView.  
[NVUnityPlugin](NVIDIA.NVUnityPlugin.html)| Provides methods to manage loading
and unloading NVIDIA module plugins.  
  
### Structs

[DLSSCommandExecutionData](NVIDIA.DLSSCommandExecutionData.html)| Represents
the state of a DLSSContext. If you call Device.ExecuteDLSS, Unity sends the
values in this struct to the runtime. After this, you can change the values in
this struct without any side effects.  
---|---  
[DLSSCommandInitializationData](NVIDIA.DLSSCommandInitializationData.html)|
Represent the initialization state of a DLSSContext. You can only use and set
this when calling GraphicsDevice.CreateFeature.  
[DLSSDebugFeatureInfos](NVIDIA.DLSSDebugFeatureInfos.html)| Represents debug
information for a particular DLSSContext.  
[DLSSTextureTable](NVIDIA.DLSSTextureTable.html)| The set of texture slots
available for the DLSSContext. SA GraphicsDevice.ExecuteDLSS  
[OptimalDLSSSettingsData](NVIDIA.OptimalDLSSSettingsData.html)| Represents the
performance settings that DLSS recommends based on the system's graphics card
and the size of the input and output color buffers. Additional resources:
GraphicsDevice.GetOptimalSettings  
  
### Enumerations

[DLSSFeatureFlags](NVIDIA.DLSSFeatureFlags.html)| Options that represent
subfeatures of DLSS.  
---|---  
[DLSSQuality](NVIDIA.DLSSQuality.html)| Options for DLSS performance modes.  
[GraphicsDeviceFeature](NVIDIA.GraphicsDeviceFeature.html)| Lists every
feature ID the GraphicsDevice API supports. For now, this only includes Deep
Learning Super Sampling (DLSS). To check if the device supports a feature,
call GraphicsDevice.IsFeatureAvailable.  
  
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

