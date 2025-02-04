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

# ISerializationCallbackReceiver

interface in UnityEngine

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

Interface for receiving callbacks before serialization and after
deserialization, to process datatypes that can't otherwise be serialized or
deserialized.

The Unity serializer can automatically serialize most data types, but not all
of them. In cases where a data type can't be serialized, you can use the
serialization callbacks defined in this interface to manually process the data
into a serializable form. For more information on when and why manual
processing is necessary, refer to [Custom serialization](../Manual/script-
serialization-custom-serialization.html).  
  
Unity invokes `OnBeforeSerialize` just before an object is serialized. Inside
this callback, you can transform your data into something Unity understands
just before Unity serializes it. After the callback is complete, Unity
serializes the arrays.  
  
Unity invokes `OnAfterDeserialize` after an object is deserialized. After
Unity has written the data to your fields, use this callback to transform the
deserialized data back into the form you want it to have at runtime.  
  
Work performed in these callbacks must be done with care, as the Unity
serializer runs on a different thread from most of the Unity API. It's
recommended to process only fields that are directly owned by the object, to
keep the processing burden as low as possible.  
  
This interface supports serialization as reference, such as on objects
decorated with the [SerializeReference](SerializeReference.html) attribute.
The order of callback execution between these objects isn't guaranteed.
However, the following execution orders are guaranteed:

  * `OnBeforeSerialize` is called on the host object before it's called on any of the host object's managed references.
  * `OnAfterDeserialize` is called on the host object before it's called on any of the host object's managed references.

For a full explanation of the `SerializeReference` attribute's behaviour,
refer to [SerializeReference](SerializeReference.html). For more information
on when and how Unity performs serialization, refer to [Script
serialization](../Manual/script-serialization.html) in the Manual.

    
    
    using UnityEngine;
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections.Generic;  
      
    public class SerializationCallbackScript : [MonoBehaviour](MonoBehaviour.html), [ISerializationCallbackReceiver](ISerializationCallbackReceiver.html)
    {
        public List<int> keys = new List<int> { 3, 4, 5 };
        public List<string> values = new List<string> { "I", "Love", "Unity" };  
      
        // Create a Dictionary. The Unity serializer doesn't support Dictionary types.
        public Dictionary<int, string>  myDictionary = new Dictionary<int, string>();  
      
        public void OnBeforeSerialize()
        {
            keys.Clear();
            values.Clear();
            // For each key/value pair in the dictionary, add the key to the keys list and the value to the values list
            foreach (var kvp in myDictionary)
            {
                keys.Add(kvp.Key);
                values.Add(kvp.Value);
            }
        }  
      
        public void OnAfterDeserialize()
        {
            myDictionary = new Dictionary<int, string>();
            // Loop through the list of keys and values and add each key/value pair to the dictionary
            for (int i = 0; i != Math.Min(keys.Count, values.Count); i++)
                myDictionary.Add(keys[i], values[i]);
        }  
      
        void OnGUI()
        {
            // This callback displays the following output on three separate labels in the GameView:
            // "Key: 3 value: I"
            // "Key: 4 value: Love"
            // "Key: 5 value: Unity"
            foreach (var kvp in myDictionary)
                [GUILayout.Label](GUILayout.Label.html)("Key: " + kvp.Key + " value: " + kvp.Value);
        }
    }
    

Additional resources: [SerializeReference](SerializeReference.html),
[SerializeField](SerializeField.html).

### Public Methods

[OnAfterDeserialize](ISerializationCallbackReceiver.OnAfterDeserialize.html)|
Implement this callback to transform data back into runtime data types after
an object is deserialized.  
---|---  
[OnBeforeSerialize](ISerializationCallbackReceiver.OnBeforeSerialize.html)|
Implement this callback to transform data into serializable data types
immediately before an object is serialized.  
  
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

