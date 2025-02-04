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

# Stage

class in UnityEditor.SceneManagement

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

The Stage class represents an editing context which includes a collection of
Scenes.

The main stage contains all the currently open regular Scenes, while a Prefab
stage contains a preview Scene used solely for editing the Prefab in.  
  
The breadcrumbs shown in the Scene view when in Prefab Mode each represent an
individual stage. Those with a Prefab icon represent Prefab stages.  
  
Additional resources: [MainStage](SceneManagement.MainStage.html),
[PreviewSceneStage](SceneManagement.PreviewSceneStage.html).

### Properties

[assetPath](SceneManagement.Stage-assetPath.html)| The path of the Asset file
associated with the stage, relative to the project root folder.  
---|---  
[stageHandle](SceneManagement.Stage-stageHandle.html)| The StageHandle struct
for this stage.  
  
### Public Methods

[FindComponentOfType](SceneManagement.Stage.FindComponentOfType.html)| Returns
the first active loaded object of the given type.  
---|---  
[FindComponentsOfType](SceneManagement.Stage.FindComponentsOfType.html)|
Returns a list of all active loaded objects of the given type.  
[GetCombinedSceneCullingMaskForCamera](SceneManagement.Stage.GetCombinedSceneCullingMaskForCamera.html)|
Gets the Scene culling mask from this Stage.  
  
### Protected Methods

[CreateHeaderContent](SceneManagement.Stage.CreateHeaderContent.html)| Creates
the header content for this Stage. Both the Hierarchy window header and Scene
view breadcrumb bar use this content.  
---|---  
[GetHashForStateStorage](SceneManagement.Stage.GetHashForStateStorage.html)|
Unity calls this method to get a hash code that is used to save the state of
the Stage to disk.  
[OnCloseStage](SceneManagement.Stage.OnCloseStage.html)| Unity calls this
method when the Stage is closed. Classes that inherit from Stage should
implement cleanup logic in this method.  
[OnDisable](SceneManagement.Stage.OnDisable.html)| See
ScriptableObject.OnDisable.  
[OnEnable](SceneManagement.Stage.OnEnable.html)| See
ScriptableObject.OnEnable.  
[OnFirstTimeOpenStageInSceneView](SceneManagement.Stage.OnFirstTimeOpenStageInSceneView.html)|
Unity calls this method the first time a Stage is opened for a specific Asset,
for a specific Scene view.  
[OnOpenStage](SceneManagement.Stage.OnOpenStage.html)| Unity calls this method
when the Stage is opened. Classes that inherit from Stage should implement
initialization logic in this method.  
[OnReturnToStage](SceneManagement.Stage.OnReturnToStage.html)| Unity calls
this method when you return to a Stage that is already open.  
  
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

