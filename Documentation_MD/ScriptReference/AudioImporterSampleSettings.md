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

# AudioImporterSampleSettings

struct in UnityEditor

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

This structure contains a collection of settings used to define how an
AudioClip should be imported.  
  
This structure is used with the AudioImporter to define how the AudioClip
should be imported and treated during loading within the Scene.

### Properties

[compressionFormat](AudioImporterSampleSettings-compressionFormat.html)|
CompressionFormat defines the compression type that the audio file is encoded
to. Different compression types have different performance and audio artifact
characteristics.  
---|---  
[loadType](AudioImporterSampleSettings-loadType.html)| LoadType defines how
the imported AudioClip data should be loaded.  
[preloadAudioData](AudioImporterSampleSettings-preloadAudioData.html)|
Preloads audio data of the clip when the clip asset is loaded. When this flag
is off, scripts have to call AudioClip.LoadAudioData() to load the data before
the clip can be played. Properties like length, channels and format are
available before the audio data has been loaded.  
[quality](AudioImporterSampleSettings-quality.html)| Audio compression quality
(0-1)Amount of compression. The value roughly corresponds to the ratio between
the resulting and the source file sizes.  
[sampleRateOverride](AudioImporterSampleSettings-sampleRateOverride.html)|
Target sample rate to convert to when samplerateSetting is set to
OverrideSampleRate.  
[sampleRateSetting](AudioImporterSampleSettings-sampleRateSetting.html)|
Defines how the sample rate is modified (if at all) of the importer audio
file.  
  
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

