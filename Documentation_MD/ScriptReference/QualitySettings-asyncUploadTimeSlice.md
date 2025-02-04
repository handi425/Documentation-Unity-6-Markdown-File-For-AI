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

#  [QualitySettings](QualitySettings.html).asyncUploadTimeSlice

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

public static int asyncUploadTimeSlice;

### Description

Async texture upload provides timesliced async texture upload on the render
thread with tight control over memory and timeslicing. There are no
allocations except for the ones which driver has to do. To read data and
upload texture data a ringbuffer whose size can be controlled is re-used.  
  
Use asyncUploadTimeSlice to set the time-slice in milliseconds for
asynchronous texture uploads per frame. Minimum value is 1 and maximum is 33.

Additional resources: [Asynchronous Texture
Upload](../Manual/LoadingTextureandMeshData.html), [Quality
Settings](../Manual/class-QualitySettings.html).

    
    
    using UnityEngine;  
      
    public class StartupExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Set [Time](Time.html) Slice to 2 ms
            [QualitySettings.asyncUploadTimeSlice](QualitySettings-asyncUploadTimeSlice.html) = 2;
        }
    }
    

Additional resources: [Quality Settings](../Manual/class-
QualitySettings.html).

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

