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

#  [QualitySettings](QualitySettings.html).asyncUploadBufferSize

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

public static int asyncUploadBufferSize;

### Description

Asynchronous texture and mesh data upload provides timesliced async texture
and mesh data upload on the render thread with tight control over memory and
timeslicing. There are no allocations except for the ones which driver has to
do. To read data and upload texture and mesh data, Unity re-uses a ringbuffer
whose size can be controlled.  
  
Use asyncUploadBufferSize to set the buffer size for asynchronous texture and
mesh data uploads. The minimum value is 2 megabytes and the maximum value is
2047 megabytes. The buffer resizes automatically to fit the largest texture
currently loading. To avoid a buffer resize (which can use extra system
resources) set this value to the size of the largest texture in the Scene. If
you have issues with excessive memory usage, you may need to reduce the value
of this buffer or disable [asyncUploadPersistentBuffer](QualitySettings-
asyncUploadPersistentBuffer.html). Memory fragmentation can occur if you
choose the latter option.

Additional resources: [Loading texture and mesh
data](../Manual/LoadingTextureandMeshData.html), [Quality
Settings](../Manual/class-QualitySettings.html).

    
    
    using UnityEngine;  
      
    public class StartupExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Set Ring Buffer Size to 16 MB.
            [QualitySettings.asyncUploadBufferSize](QualitySettings-asyncUploadBufferSize.html) = 16;
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

