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

# WriteAccessRequiredAttribute

class in Unity.Collections.LowLevel.Unsafe

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

Specify which struct method and property requires write access to be invoked.

Used in conjunction with the
[ReadOnlyAttribute](Unity.Collections.ReadOnlyAttribute.html),
WriteAccessRequiredAttribute lets you specify which struct method and property
requires write access to be invoked. When you add the
[ReadOnly](Unity.Collections.NativeArray_1.ReadOnly.html) attribute to a
native container, it indicates that only operations that read data can be
performed on the native container, and you can't use methods and properties on
the native container that modify the array. The `WriteAccessRequired`
attribute indicates which methods and properties can't be used on a native
container with the [ReadOnly](Unity.Collections.NativeArray_1.ReadOnly.html)
attribute.

    
    
    using Unity.Collections.LowLevel.Unsafe;
    using Unity.Collections;
    using UnityEngine;  
      
    [NativeContainer]
    public struct MyList<T> where T : struct
    {
        public int [Length](UIElements.Length.html) { get; private set; }  
      
        [WriteAccessRequired]
        public void Grow(int capacity)
        {
            // ...
        }
    }  
      
    public class MyMonoBehaviour : [MonoBehaviour](MonoBehaviour.html)
    {
        [[ReadOnly](Unity.Collections.NativeArray_1.ReadOnly.html)]
        MyList<int> readOnlyList;  
      
        MyList<int> writableList = new MyList<int>();  
      
        public void OnUpdate()
        {
            writableList.Grow(10); // Ok
            readOnlyList.Grow(10); // Illegal
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

