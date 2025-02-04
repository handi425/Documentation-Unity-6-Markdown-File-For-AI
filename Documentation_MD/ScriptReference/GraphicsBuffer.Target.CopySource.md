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

#  [GraphicsBuffer.Target](GraphicsBuffer.Target.html).CopySource

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

GraphicsBuffer can be used as a source for CopyBuffer.

The source buffer for [Graphics.CopyBuffer](Graphics.CopyBuffer.html) or
[CommandBuffer.CopyBuffer](Rendering.CommandBuffer.CopyBuffer.html) must have
`CopySource` target set. This target is most often combined with other target
flags.

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // create a source index buffer and set data for it
            var src = new [GraphicsBuffer](GraphicsBuffer.html)(
                [GraphicsBuffer.Target.Index](GraphicsBuffer.Target.Index.html) | [GraphicsBuffer.Target.CopySource](GraphicsBuffer.Target.CopySource.html),
                3, 2);
            src.SetData(new ushort[] {1, 10, 100});
            // create a destination index buffer and copy source into it
            var dst = new [GraphicsBuffer](GraphicsBuffer.html)(
                [GraphicsBuffer.Target.Index](GraphicsBuffer.Target.Index.html) | [GraphicsBuffer.Target.CopyDestination](GraphicsBuffer.Target.CopyDestination.html),
                3, 2);
            [Graphics.CopyBuffer](Graphics.CopyBuffer.html)(src, dst);  
      
            // check the copied data
            var got = new ushort[3];
            dst.GetData(got);
            [Debug.Log](Debug.Log.html)($"copied data: {got[0]}, {got[1]}, {got[2]}");  
      
            // release the buffers
            src.Release();
            dst.Release();
        }
    }
    

Additional resources: [Graphics.CopyBuffer](Graphics.CopyBuffer.html),
[CommandBuffer.CopyBuffer](Rendering.CommandBuffer.CopyBuffer.html),
[GraphicsBuffer.Target.CopyDestination](GraphicsBuffer.Target.CopyDestination.html).

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

