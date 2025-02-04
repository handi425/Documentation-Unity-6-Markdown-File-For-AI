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

# ScriptableSingleton<T0>

class in UnityEditor

/

Inherits from:[ScriptableObject](ScriptableObject.html)

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

Generic class for storing Editor state.

The ScriptableSingleton generic class allows you to create 'Manager' type
classes in the Unity Editor. In classes that derive from ScriptableSingleton,
serializable data you add survives assembly reloading in the Editor. Also, if
the class uses the [FilePathAttribute](FilePathAttribute.html), the
serializable data persists between sessions of Unity.

    
    
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    [FilePath("SomeSubFolder/StateFile.foo", [FilePathAttribute.Location.PreferencesFolder](FilePathAttribute.Location.PreferencesFolder.html))]
    public class MySingleton : ScriptableSingleton<MySingleton>
    {
        [[SerializeField](SerializeField.html)]
        float m_Number = 42;  
      
        [[SerializeField](SerializeField.html)]
        List<string> m_Strings = new List<string>();  
      
        public void Modify()
        {
            m_Number *= 2;
            m_Strings.Add("Foo" + m_Number);  
      
            Save(true);
            [Debug.Log](Debug.Log.html)("Saved to: " + GetFilePath());
        }  
      
        public void Log()
        {
            [Debug.Log](Debug.Log.html)("MySingleton state: " + [JsonUtility.ToJson](JsonUtility.ToJson.html)(this, true));
        }
    }  
      
    
    static class MySingletonMenuItems
    {
        [[MenuItem](MenuItem.html)("SingletonTest/Log")]
        static void LogMySingletonState()
        {
            MySingleton.instance.Log();
        }  
      
        [[MenuItem](MenuItem.html)("SingletonTest/Modify")]
        static void ModifyMySingletonState()
        {
            MySingleton.instance.Modify();
        }
    }
    

### Static Properties

[instance](ScriptableSingleton_1-instance.html)| Gets the instance of the
Singleton. Unity creates the Singleton instance when this property is accessed
for the first time. If you use the FilePathAttribute, then Unity loads the
data on the first access as well.  
---|---  
  
### Protected Methods

[Save](ScriptableSingleton_1.Save.html)| Saves the current state of the
ScriptableSingleton.  
---|---  
  
### Static Methods

[GetFilePath](ScriptableSingleton_1.GetFilePath.html)| Get the file path where
this ScriptableSingleton is saved to.  
---|---  
  
### Inherited Members

### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
[CreateInstance](ScriptableObject.CreateInstance.html)| Creates an instance of
a scriptable object.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
### Messages

[Awake](ScriptableObject.Awake.html)| Called when an instance of
ScriptableObject is created.  
---|---  
[OnDestroy](ScriptableObject.OnDestroy.html)| This function is called when the
scriptable object will be destroyed.  
[OnDisable](ScriptableObject.OnDisable.html)| This function is called when the
scriptable object goes out of scope.  
[OnEnable](ScriptableObject.OnEnable.html)| This function is called when the
object is loaded.  
[OnValidate](ScriptableObject.OnValidate.html)| Editor-only function that
Unity calls when the script is loaded or a value changes in the Inspector.  
[Reset](ScriptableObject.Reset.html)| Reset to default values.  
  
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

