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

# H264EncoderAttributes

struct in UnityEditor.Media

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

Descriptor for H.264 encoder attributes.

    
    
    using UnityEditor.Media;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using Unity.Collections;
    using System.IO;  
      
    public class [Recorder](Profiling.Recorder.html)
    {
        static public void RecordMovie()
        {
            [H264EncoderAttributes](Media.H264EncoderAttributes.html) h264Attr = new [H264EncoderAttributes](Media.H264EncoderAttributes.html)
            {
                gopSize = 25,
                numConsecutiveBFrames = 2,
                profile = [VideoEncodingProfile.H264High](VideoEncodingProfile.H264High.html)
            };  
      
            var videoAttr = new [VideoTrackEncoderAttributes](Media.VideoTrackEncoderAttributes.html)(h264Attr)
            {
                frameRate = new [MediaRational](Media.MediaRational.html)(50),
                width = 320,
                height = 200,
                targetBitRate = 3000000
            };  
      
            var audioAttr = new [AudioTrackAttributes](Media.AudioTrackAttributes.html)
            {
                sampleRate = new [MediaRational](Media.MediaRational.html)(48000),
                channelCount = 2,
                language = "fr"
            };  
      
            int sampleFramesPerVideoFrame = audioAttr.channelCount *
                audioAttr.sampleRate.numerator / videoAttr.frameRate.numerator;  
      
            var encodedFilePath = Path.Combine(Path.GetTempPath(), "my_movie.mp4");  
      
            [Texture2D](Texture2D.html) tex = new [Texture2D](Texture2D.html)((int)videoAttr.width, (int)videoAttr.height, [TextureFormat.RGBA32](TextureFormat.RGBA32.html), false);  
      
            using (var encoder = new [MediaEncoder](Media.MediaEncoder.html)(encodedFilePath, videoAttr, audioAttr))
            using (var audioBuffer = new NativeArray<float>(sampleFramesPerVideoFrame, [Allocator.Temp](Unity.Collections.Allocator.Temp.html)))
            {
                for (int i = 0; i < 100; ++i)
                {
                    // Fill 'tex' with the video content to be encoded into the file for this frame.
                    // ...
                    encoder.AddFrame(tex);  
      
                    // Fill 'audioBuffer' with the audio content to be encoded into the file for this frame.
                    // ...
                    encoder.AddSamples(audioBuffer);
                }
            }
        }
    }
    

### Properties

[gopSize](Media.H264EncoderAttributes-gopSize.html)| The maximum size of a
group of pictures, in frames.  
---|---  
[numConsecutiveBFrames](Media.H264EncoderAttributes-
numConsecutiveBFrames.html)| The maximum number of consecutive B frames
between I and P frames.  
[profile](Media.H264EncoderAttributes-profile.html)| The VideoEncodingProfile
for the encoded video.  
  
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

