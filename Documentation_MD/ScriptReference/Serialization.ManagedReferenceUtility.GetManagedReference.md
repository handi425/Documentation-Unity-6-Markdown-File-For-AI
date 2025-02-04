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

#
[ManagedReferenceUtility](Serialization.ManagedReferenceUtility.html).GetManagedReference

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

## Declaration

public static object GetManagedReference([Object](Object.html) obj, long id);

### Parameters

hostObj | The host object that supports [SerializeReference](SerializeReference.html). For example, [MonoBehaviour](MonoBehaviour.html) or [ScriptableObject](ScriptableObject.html).  
---|---  
refId | The managed reference Id.  
  
### Returns

**object** Returns the C# object referenced on the specified host and
identified with provided Id. Returns null if no reference object is found.

### Description

Retrieves an object based on its managed reference Id.

Use this method to efficiently retrieve a specific referenced object when, for
example, its exact location within an array or graph is unknown.  
  
Additional resources:
[GetManagedReferenceIdForObject](Serialization.ManagedReferenceUtility.GetManagedReferenceIdForObject.html),
[SerializeReference](SerializeReference.html).

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using UnityEngine.Serialization;  
      
    public class GetManagedReferenceExample : [ScriptableObject](ScriptableObject.html)
    {
        [Serializable]
        public class [Item](Progress.Item.html)
        {
            public char m_data;
        }  
      
        [[SerializeReference](SerializeReference.html)]
        public List<[Item](Progress.Item.html)> m_items = new List<[Item](Progress.Item.html)>();  
      
        private void InsertNewItem(long id, char data)
        {
            var newItem = new [Item](Progress.Item.html)() {m_data = data};
            if ([ManagedReferenceUtility.SetManagedReferenceIdForObject](Serialization.ManagedReferenceUtility.SetManagedReferenceIdForObject.html)(this, newItem, id))
                m_items.Add(newItem);
        }  
      
        [[MenuItem](MenuItem.html)("Example/[ManagedReferenceUtility](Serialization.ManagedReferenceUtility.html) GetManagedReference Example")]
        static void TestMethod()
        {
            var scriptableObject = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<GetManagedReferenceExample>();  
      
            scriptableObject.InsertNewItem(1000, 'a');
            scriptableObject.InsertNewItem(1001, 'b');
            scriptableObject.InsertNewItem(1002, 'c');
            scriptableObject.InsertNewItem(1003, 'd');  
      
            // Because 1002 is registered in an earlier call this will log an error and not change the state
            scriptableObject.InsertNewItem(1002, 'e');  
      
            // The array may get reordered over time.  One way to find an specific item again would
            // be to look it up based on a known managed reference id
            var item = [ManagedReferenceUtility.GetManagedReference](Serialization.ManagedReferenceUtility.GetManagedReference.html)(scriptableObject, 1002) as [Item](Progress.Item.html);
            [Debug.LogFormat](Debug.LogFormat.html)("[Data](Unity.Android.Gradle.Manifest.Data.html) on object 1002 is {0}", item.m_data);  
      
            var willBeNull = [ManagedReferenceUtility.GetManagedReference](Serialization.ManagedReferenceUtility.GetManagedReference.html)(scriptableObject, 9999) as [Item](Progress.Item.html);
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

