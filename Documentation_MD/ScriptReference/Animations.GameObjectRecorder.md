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

# GameObjectRecorder

class in UnityEditor.Animations

/

Inherits from:[Object](Object.html)

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

Records the changing properties of a [GameObject](GameObject.html) as the
Scene runs and saves the information into an
[AnimationClip](AnimationClip.html).

This class binds [GameObject](GameObject.html) properties, records their
values as they change in the running Scene, and saves the result in an
[AnimationClip](AnimationClip.html). The recorded GameObject is called
[root](Animations.GameObjectRecorder-root.html) in the class, and you can also
bind the properties of any child of [root](Animations.GameObjectRecorder-
root.html).  
  
See the following code example on how this class can be implemented and to set
what gets recorded.

    
    
    using UnityEngine;
    using UnityEditor.Animations;  
      
    public class RecordTransformHierarchy : [MonoBehaviour](MonoBehaviour.html)
    {
        public [AnimationClip](AnimationClip.html) clip;  
      
        private [GameObjectRecorder](Animations.GameObjectRecorder.html) m_Recorder;  
      
        void Start()
        {
            // Create recorder and record the script [GameObject](GameObject.html).
            m_Recorder = new [GameObjectRecorder](Animations.GameObjectRecorder.html)(gameObject);  
      
            // Bind all the Transforms on the [GameObject](GameObject.html) and all its children.
            m_Recorder.BindComponentsOfType<[Transform](Transform.html)>(gameObject, true);
        }  
      
        void LateUpdate()
        {
            if (clip == null)
                return;  
      
            // Take a snapshot and record all the bindings values for this frame.
            m_Recorder.TakeSnapshot([Time.deltaTime](Time-deltaTime.html));
        }  
      
        void OnDisable()
        {
            if (clip == null)
                return;  
      
            if (m_Recorder.isRecording)
            {
                // Save the recorded session to the clip.
                m_Recorder.SaveToClip(clip);
            }
        }
    }
    

### Properties

[currentTime](Animations.GameObjectRecorder-currentTime.html)| Returns the
current time of the recording. (Read Only)  
---|---  
[isRecording](Animations.GameObjectRecorder-isRecording.html)| Returns true
when the recorder is recording. (Read Only)  
[root](Animations.GameObjectRecorder-root.html)| The GameObject root of the
animated hierarchy. (Read Only)  
  
### Constructors

[GameObjectRecorder](Animations.GameObjectRecorder-ctor.html)| Create a new
GameObjectRecorder.  
---|---  
  
### Public Methods

[Bind](Animations.GameObjectRecorder.Bind.html)| Binds a GameObject's property
as defined by EditorCurveBinding.  
---|---  
[BindAll](Animations.GameObjectRecorder.BindAll.html)| Adds bindings for all
of target's properties, and also for all the target's children if recursive is
true.  
[BindComponent](Animations.GameObjectRecorder.BindComponent.html)| Adds
bindings for all the properties of component.  
[BindComponentsOfType](Animations.GameObjectRecorder.BindComponentsOfType.html)|
Adds bindings for all the properties of the first component of type T found in
target, and also for all the target's children if recursive is true.  
[GetBindings](Animations.GameObjectRecorder.GetBindings.html)| Returns an
array of all the bindings added to the recorder.  
[ResetRecording](Animations.GameObjectRecorder.ResetRecording.html)| Reset the
recording.  
[SaveToClip](Animations.GameObjectRecorder.SaveToClip.html)| Saves recorded
animation to a destination clip.  
[TakeSnapshot](Animations.GameObjectRecorder.TakeSnapshot.html)| Forwards the
animation by dt seconds, then record the values of the added bindings.  
  
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

