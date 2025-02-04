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

#  [QualitySettings](QualitySettings.html).asyncUploadPersistentBuffer

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

public static bool asyncUploadPersistentBuffer;

### Description

This flag controls if the async upload pipeline's ring buffer remains
allocated when there are no active loading operations. Set this to true, to
make the ring buffer allocation persist after all upload operations have
completed. If you have issues with excessive memory usage, you can set this to
false. This means you reduce the runtime memory footprint, but memory
fragmentation can occur. The default value is true.

Additional resources: [Loading texture and mesh
data](../Manual/LoadingTextureandMeshData.html), [Quality
Settings](../Manual/class-QualitySettings.html).

    
    
    using UnityEngine;
    public class StartupExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // The upload buffer will be deallocated when all uploads are complete.
            [QualitySettings.asyncUploadPersistentBuffer](QualitySettings-asyncUploadPersistentBuffer.html) = false;
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

