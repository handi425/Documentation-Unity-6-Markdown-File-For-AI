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

# Object

class in UnityEngine

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

[Switch to Manual](../Manual/class-Object.html "Go to Object Component in the
Manual")

### Description

Base class for all objects Unity can reference.

UnityEngine.Object is the base class of all built-in Unity objects. Custom
Unity Object types can be defined in scripts by deriving a new class from
types like [MonoBehaviour](MonoBehaviour.html),
[ScriptableObject](ScriptableObject.html) and
[ScriptedImporter](AssetImporters.ScriptedImporter.html).  
  
Any public variable you make that derives from Object gets shown in the
inspector as a drop target, allowing you to set the value from the GUI.  
  
Typically scripts will use types derived from this class, for example
[GameObject](GameObject.html), [Material](Material.html) and
[Mesh](Mesh.html), so that the specific properties and methods for those types
are exposed to the script. However, some APIs are designed to work with any
Unity Object, so Object appears as a type in their signatures. For example
[Resources.LoadAll](Resources.LoadAll.html),
[EditorJsonUtility.ToJson](EditorJsonUtility.ToJson.html) and
[SerializedObject](SerializedObject.html).  
  
Sometimes an instance of Object can be in a detached state, where there is no
underlying native object. This can happen if the instance references an native
object that has been destroyed, or a missing Asset or missing type. Detached
objects retain their InstanceID, but the object cannot be used to call methods
or access properties. An object in this state will appear to be null, because
of special implementations of operator ==, operator != and
[Object.bool](Object-operator_Object.html). Because the object is not truly
null, a call to **Object.ReferenceEquals(myobject, null)** will return false.  
  
The [null-conditional operator ](https://docs.microsoft.com/en-
us/dotnet/csharp/language-reference/language-specification/expressions#null-
conditional-operator) (**?.**) and the [null-coalescing operator
](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/language-
specification/expressions#the-null-coalescing-operator)(**??**) are not
supported with Unity Objects because they cannot be overridden to treat
detached objects objects the same as null. It is only safe to use those
operators in your scripts if there is certainty that the objects being checked
are never in a detached state.

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
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
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

