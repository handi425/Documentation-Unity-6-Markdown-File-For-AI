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

#  [QualitySettings](QualitySettings.html).streamingMipmapsRenderersPerFrame

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

[Switch to Manual](../Manual/class-QualitySettings.html "Go to QualitySettings
Component in the Manual")

public static int streamingMipmapsRenderersPerFrame;

### Description

The number of renderer instances that are processed each frame when
calculating which texture mipmap levels should be streamed.

If the number of renderers exceeds this limit, the mipmap levels of the
textures associated with those additional renderers are calculated in
subsequent frames.  
  
Lower this value to reduce the CPU cost of calculating the optimal mipmap
levels. The tradeoff is that a lower value also reduces the rate of texture
mipmap computation and the loading of those desired mipmaps.  
  
By default, the initial value is 512, but this can be set in the
[Quality](../Manual/class-QualitySettings.html) section of the Editor
**Project Settings** window, under **Textures** > **Mipmap Streaming**.  
  
Note: Do not change `streamingMipmapsRenderersPerFrame` too frequently at
runtime. You should allow enough time between changes for all the renderers to
be processed. Updating this value more frequently will lead to unused mips
remaining loaded. The following example illustrates how to calculate the
number of frames to delay between changes:

    
    
    using System.Collections;
    using UnityEngine;
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        int nextUpdateAllowed = 0;
        int _renderersPerFrame;  
      
        // Increase this value when frame rate is high, lower when frame rate drops)
        public int RenderersPerFrame
        {
            get { return [QualitySettings.streamingMipmapsRenderersPerFrame](QualitySettings-streamingMipmapsRenderersPerFrame.html); }
            set
            {
                _renderersPerFrame = value;
                StopCoroutine("UpdateRenderCount");
                StartCoroutine("UpdateRenderCount");
            }
        }  
      
        IEnumerator UpdateRenderCount()
        {
            while ([Time.frameCount](Time-frameCount.html) < nextUpdateAllowed)
                yield return null;  
      
            [QualitySettings.streamingMipmapsRenderersPerFrame](QualitySettings-streamingMipmapsRenderersPerFrame.html) = _renderersPerFrame;
            int frameDelay = (int)([Texture.streamingRendererCount](Texture-streamingRendererCount.html) + (ulong)(_renderersPerFrame - 1)) / _renderersPerFrame;
            nextUpdateAllowed = [Time.frameCount](Time-frameCount.html) + frameDelay;  
      
            yield return null;
        }
    }
    

Additional resources: [Texture.streamingRendererCount](Texture-
streamingRendererCount.html).

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

