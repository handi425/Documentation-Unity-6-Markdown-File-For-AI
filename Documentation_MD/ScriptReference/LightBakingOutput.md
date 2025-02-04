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

# LightBakingOutput

struct in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Struct describing the result of a Global Illumination bake for a given light.

The example below demonstrates how you can check the baked status of a light
and change its active state.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class LightBakingOutputExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void TurnOffLight([Light](Light.html) light)
        {
            if (light.bakingOutput.isBaked && light.bakingOutput.lightmapBakeType != [LightmapBakeType.Realtime](LightmapBakeType.Realtime.html))
            {
                [Debug.Log](Debug.Log.html)("[Light](Light.html) got some contribution statically baked, it cannot be turned off at runtime.");
            }
            else
            {
                light.enabled = false;
            }
        }
    }
    

### Properties

[isBaked](LightBakingOutput-isBaked.html)| Is the light contribution already
stored in lightmaps and/or lightprobes?  
---|---  
[lightmapBakeType](LightBakingOutput-lightmapBakeType.html)| This property
describes what part of a light's contribution was baked.  
[mixedLightingMode](LightBakingOutput-mixedLightingMode.html)| In case of a
LightmapBakeType.Mixed light, describes what Mixed mode was used to bake the
light, irrelevant otherwise.  
[occlusionMaskChannel](LightBakingOutput-occlusionMaskChannel.html)| In case
of a LightmapBakeType.Mixed light, contains the index of the occlusion mask
channel to use if any, otherwise -1.  
[probeOcclusionLightIndex](LightBakingOutput-probeOcclusionLightIndex.html)|
In case of a LightmapBakeType.Mixed light, contains the index of the light as
seen from the occlusion probes point of view if any, otherwise -1.  
  
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

