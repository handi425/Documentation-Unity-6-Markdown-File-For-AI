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

# VisualTreeAsset

class in UnityEngine.UIElements

/

Inherits from:[ScriptableObject](ScriptableObject.html)

/

Implemented
in:[UnityEngine.UIElementsModule](UnityEngine.UIElementsModule.html)

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

An instance of this class holds a tree of `VisualElementAsset's`, created from
a UXML file. Each node in the file corresponds to a `VisualElementAsset`. You
can clone a `VisualTreeAsset` to create a tree of `VisualElement's`.  
  
**Note** : You can't generate a `VisualTreeAsset` from raw UXML at runtime.

### Properties

[contentHash](UIElements.VisualTreeAsset-contentHash.html)|  A hash value
computed from the template content.  
---|---  
[importedWithErrors](UIElements.VisualTreeAsset-importedWithErrors.html)|
Whether there were errors encountered while importing the UXML File  
[importedWithWarnings](UIElements.VisualTreeAsset-importedWithWarnings.html)|
Whether there were warnings encountered while importing the UXML File  
[stylesheets](UIElements.VisualTreeAsset-stylesheets.html)|  The stylesheets
used by this VisualTreeAsset.  
[templateDependencies](UIElements.VisualTreeAsset-templateDependencies.html)|
The UXML templates used by this VisualTreeAsset.  
  
### Public Methods

[CloneTree](UIElements.VisualTreeAsset.CloneTree.html)|  Build a tree of
VisualElements from the asset.  
---|---  
[Instantiate](UIElements.VisualTreeAsset.Instantiate.html)|  Build a tree of
VisualElements from the asset.  
  
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

