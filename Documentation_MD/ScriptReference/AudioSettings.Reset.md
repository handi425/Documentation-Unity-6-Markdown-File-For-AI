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

#  [AudioSettings](AudioSettings.html).Reset

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

[Switch to Manual](../Manual/class-AudioSettings.html "Go to AudioSettings
Component in the Manual")

## Declaration

public static bool Reset([AudioConfiguration](AudioConfiguration.html)
config);

### Parameters

config | The new configuration to be used.  
---|---  
  
### Returns

**bool** True if all settings could be successfully applied.

### Description

Changes the device configuration and invokes the
[AudioSettings.OnAudioConfigurationChanged](AudioSettings.OnAudioConfigurationChanged.html)
delegate with the argument `deviceWasChanged=false`. There's no guarantee that
the exact settings specified are used, but Unity automatically uses the
closest match that it supports. **Note:** This can cause main thread stalls if
`AudioSettings.Reset` is called when objects are loading asynchronously.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class TestAudioConfiguration : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [AudioSettings.OnAudioConfigurationChanged](AudioSettings.OnAudioConfigurationChanged.html) += OnAudioConfigurationChanged;
        }  
      
        void OnAudioConfigurationChanged(bool deviceWasChanged)
        {
            [Debug.Log](Debug.Log.html)(deviceWasChanged ? "[Device](tvOS.Device.html) was changed" : "Reset was called");
            if (deviceWasChanged)
            {
                [AudioConfiguration](AudioConfiguration.html) config = [AudioSettings.GetConfiguration](AudioSettings.GetConfiguration.html)();
                config.dspBufferSize = 64;
                [AudioSettings.Reset](AudioSettings.Reset.html)(config);
            }
            GetComponent<[AudioSource](AudioSource.html)>().Play();
        }  
      
        static int[] validSpeakerModes =
        {
            (int)[AudioSpeakerMode.Mono](AudioSpeakerMode.Mono.html),
            (int)[AudioSpeakerMode.Stereo](AudioSpeakerMode.Stereo.html),
            (int)[AudioSpeakerMode.Quad](AudioSpeakerMode.Quad.html),
            (int)[AudioSpeakerMode.Surround](AudioSpeakerMode.Surround.html),
            (int)[AudioSpeakerMode.Mode5point1](AudioSpeakerMode.Mode5point1.html),
            (int)[AudioSpeakerMode.Mode7point1](AudioSpeakerMode.Mode7point1.html)
        };  
      
        static int[] validDSPBufferSizes =
        {
            32, 64, 128, 256, 340, 480, 512, 1024, 2048, 4096, 8192
        };  
      
        static int[] validSampleRates =
        {
            11025, 22050, 44100, 48000, 88200, 96000,
        };  
      
        static int[] validNumRealVoices =
        {
            1, 2, 4, 8, 16, 32, 50, 64, 100, 128, 256, 512,
        };  
      
        static int[] validNumVirtualVoices =
        {
            1, 2, 4, 8, 16, 32, 50, 64, 100, 128, 256, 512,
        };  
      
        int GUIRow(string name, int[] valid, int value, ref bool modified)
        {
            [GUILayout.BeginHorizontal](GUILayout.BeginHorizontal.html)();
            [GUILayout.Button](GUILayout.Button.html)(name + "=" + value);
            for (int i = 0; i < valid.Length; i++)
            {
                string s = valid[i].ToString();
                if (valid[i] == value)
                    s = "[" + s + "]";
                if ([GUILayout.Button](GUILayout.Button.html)(s))
                {
                    value = valid[i];
                    modified = true;
                }
            }
            [GUILayout.EndHorizontal](GUILayout.EndHorizontal.html)();
            return value;
        }  
      
        void OnGUI()
        {
            [AudioSource](AudioSource.html) source = GetComponent<[AudioSource](AudioSource.html)>();
            bool modified = false;  
      
            [AudioConfiguration](AudioConfiguration.html) config = [AudioSettings.GetConfiguration](AudioSettings.GetConfiguration.html)();  
      
            config.speakerMode = ([AudioSpeakerMode](AudioSpeakerMode.html))GUIRow("speakerMode", validSpeakerModes, (int)config.speakerMode, ref modified);
            config.dspBufferSize = GUIRow("dspBufferSize", validDSPBufferSizes, config.dspBufferSize, ref modified);
            config.sampleRate = GUIRow("sampleRate", validSampleRates, config.sampleRate, ref modified);
            config.numRealVoices = GUIRow("RealVoices", validNumRealVoices, config.numRealVoices, ref modified);
            config.numVirtualVoices = GUIRow("numVirtualVoices", validNumVirtualVoices, config.numVirtualVoices, ref modified);  
      
            if (modified)
                [AudioSettings.Reset](AudioSettings.Reset.html)(config);  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Start"))
                source.Play();  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Stop"))
                source.Stop();
        }
    }
    

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

