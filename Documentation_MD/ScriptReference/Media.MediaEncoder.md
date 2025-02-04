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

# MediaEncoder

class in UnityEditor.Media

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

Encodes images and audio samples into an audio or movie file.

Constructing an instance of this class creates an encoder that will create an
audio, video or audio/video file with the specified tracks in it.  
  
Call the AddFrame() and AddSamples() methods alternately for each track, so
that frames and samples keep each track equally filled.  
  
Once all the wanted frames and samples are added to the file, call Dispose()
to end each track properly and close the file.

    
    
    using UnityEditor.Media;
    using UnityEngine;
    using Unity.Collections;
    using System.IO;  
      
    public class [Recorder](Profiling.Recorder.html)
    {
        static public void RecordMovie()
        {
            var videoAttr = new [VideoTrackAttributes](Media.VideoTrackAttributes.html)
            {
                frameRate = new [MediaRational](Media.MediaRational.html)(50),
                width = 320,
                height = 200,
                includeAlpha = false
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
    

### Constructors

[MediaEncoder](Media.MediaEncoder-ctor.html)| Create a new encoder with
various track arrangements.  
---|---  
  
### Public Methods

[AddFrame](Media.MediaEncoder.AddFrame.html)| Appends a frame to the file's
video track.  
---|---  
[AddSamples](Media.MediaEncoder.AddSamples.html)| Appends sample frames to the
specified audio track.  
[Dispose](Media.MediaEncoder.Dispose.html)| Finishes writing all tracks and
closes the file being written.  
  
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

