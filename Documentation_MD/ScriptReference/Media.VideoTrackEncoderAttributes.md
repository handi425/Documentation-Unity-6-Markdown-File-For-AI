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

# VideoTrackEncoderAttributes

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

Descriptor for video track format.

    
    
    using UnityEditor.Media;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class [Recorder](Profiling.Recorder.html)
    {
        public [VideoTrackEncoderAttributes](Media.VideoTrackEncoderAttributes.html) CreateEncoderAttributes()
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
      
            return videoAttr;
        }
    }
    

### Properties

[bitRateMode](Media.VideoTrackEncoderAttributes-bitRateMode.html)| The
VideoBitrateMode for the encoded video.  
---|---  
[frameRate](Media.VideoTrackEncoderAttributes-frameRate.html)| The frame rate
for the encoded video, in frames per second, expressed as a fraction.  
[height](Media.VideoTrackEncoderAttributes-height.html)| The image height in
pixels.  
[includeAlpha](Media.VideoTrackEncoderAttributes-includeAlpha.html)| True if
the track is to include the alpha channel found in the texture passed to
AddFrame. False otherwise.  
[targetBitRate](Media.VideoTrackEncoderAttributes-targetBitRate.html)| The
target bit rate for the encoder.  
[width](Media.VideoTrackEncoderAttributes-width.html)| The image width in
pixels.  
  
### Constructors

[VideoTrackEncoderAttributes](Media.VideoTrackEncoderAttributes-ctor.html)|
Create a new VideoTrackEncoderAttributes with specific H.264 encoding options.  
---|---  
  
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

