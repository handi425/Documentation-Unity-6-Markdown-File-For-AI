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
[ManagedReferenceUtility](Serialization.ManagedReferenceUtility.html).GetManagedReferenceIds

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

public static long[] GetManagedReferenceIds([Object](Object.html) obj);

### Parameters

hostObj | The host object that supports [SerializeReference](SerializeReference.html). For example, [MonoBehaviour](MonoBehaviour.html) or [ScriptableObject](ScriptableObject.html).  
---|---  
  
### Returns

**long[]** Returns a list of the most recent serialization of the host object,
including the most recent call to
[ManagedReferenceUtility.SetManagedReferenceIdForObject](Serialization.ManagedReferenceUtility.SetManagedReferenceIdForObject.html).  
  
An entry in the list is returned as
[ManagedReferenceUtility.RefIdNull](Serialization.ManagedReferenceUtility.RefIdNull.html)
if its SerialReference field is set to null.  
  
The returned list excludes objects with missing types since they cannot be
deserialized. To retrieve objects with missing types, use
[SerializationUtility.GetManagedReferencesWithMissingTypes](SerializationUtility.GetManagedReferencesWithMissingTypes.html).

### Description

Retrieves a list of managed reference Ids assigned to objects that are
referenced using [SerializeReference](SerializeReference.html) on a specified
host.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections.Generic;
    using System.Text;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using UnityEngine.Serialization;  
      
    public class GetManagedReferenceIdsExample : [ScriptableObject](ScriptableObject.html)
    {
        [Serializable]
        public class [Item](Progress.Item.html)
        {
            public char m_data;
        }  
      
        [[SerializeReference](SerializeReference.html)]
        public [Item](Progress.Item.html) m_singleItem;  
      
        [[SerializeReference](SerializeReference.html)]
        public List<[Item](Progress.Item.html)> m_items;  
      
        [[SerializeReference](SerializeReference.html)]
        public List<[Item](Progress.Item.html)> m_secondaryList;  
      
        void PopulateState()
        {
            m_singleItem = new [Item](Progress.Item.html)() {m_data = 'a'};  
      
            m_items = new List<[Item](Progress.Item.html)>()
            {
                new [Item](Progress.Item.html)() {m_data = 'b'},
                new [Item](Progress.Item.html)() {m_data = 'c'},
                new [Item](Progress.Item.html)() {m_data = 'd'}
            };  
      
            m_secondaryList = new List<[Item](Progress.Item.html)>()
            {
                new [Item](Progress.Item.html)() {m_data = 'e'},
                new [Item](Progress.Item.html)() {m_data = 'f'}
            };  
      
            // Add some duplicates entries that point to the same instances
            m_items.Add(m_items[0]);
            m_items.Add(m_items[2]);
            m_items.Add(m_secondaryList[0]);
            m_secondaryList.Add(m_items[1]);
        }  
      
        void Serialize()
        {
            // Force a serialization of the [ScriptableObject](ScriptableObject.html) by creating a temporary [SerializedObject](SerializedObject.html) (similar to viewing the object in the inspector)
            // This ensures that all the managed references get registered and assigned Ids based on the current state.
            // Serialization also happens when a [Scene](SceneManagement.Scene.html) is saved, [Undo.RecordObjects](Undo.RecordObjects.html)() etc
            var serializedObject = new [SerializedObject](SerializedObject.html)(this);
        }  
      
        void FindAllItems()
        {
            // Get the list of Ids (accurate to state the last time this [ScriptableObject](ScriptableObject.html) was serialized).
            // This is a quick way to access all the instances across all fields, without duplicates.
            var allReferencedObjects = [ManagedReferenceUtility.GetManagedReferenceIds](Serialization.ManagedReferenceUtility.GetManagedReferenceIds.html)(this);  
      
            var objectListing = new StringBuilder();
            foreach (var id in allReferencedObjects)
            {
                if (id == SerializationUtility.RefIdNull)
                    continue;  
      
                // Lookup up the object associated with the Id.  If the [ScriptableObject](ScriptableObject.html) contained other types of referenced
                // objects that are not related to "[Item](Progress.Item.html)" class then null would be expected.
                var retrievedItem = [ManagedReferenceUtility.GetManagedReference](Serialization.ManagedReferenceUtility.GetManagedReference.html)(this, id) as [Item](Progress.Item.html);
                if (retrievedItem == null)
                    continue;  
      
                objectListing.Append("Found [Item](Progress.Item.html) object with data " + retrievedItem.m_data + " at Id " + id).AppendLine();
            }
            /*
            Output will be something like this, with the Ids different each time:  
      
            Found [Item](Progress.Item.html) object with data a at id 1757967572722253824
            Found [Item](Progress.Item.html) object with data b at id 1757967572722253825
            Found [Item](Progress.Item.html) object with data c at id 1757967572722253826
            Found [Item](Progress.Item.html) object with data d at id 1757967572722253827
            Found [Item](Progress.Item.html) object with data e at id 1757967572722253828
            Found [Item](Progress.Item.html) object with data f at id 1757967572722253829
            */
            [Debug.LogFormat](Debug.LogFormat.html)(objectListing.ToString());
        }  
      
        [[MenuItem](MenuItem.html)("Example/[ManagedReferenceUtility](Serialization.ManagedReferenceUtility.html) GetManagedReferenceIds Example")]
        static void TestMethod()
        {
            var scriptableObject = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<GetManagedReferenceIdsExample>();
            scriptableObject.PopulateState();
            scriptableObject.Serialize();
            scriptableObject.FindAllItems();
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

