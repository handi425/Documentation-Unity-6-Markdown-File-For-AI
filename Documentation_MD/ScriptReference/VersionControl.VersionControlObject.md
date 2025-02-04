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

# VersionControlObject

class in UnityEditor.VersionControl

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

The abstract base class for representing a version control system.

You can add support for a custom VCS by creating a new class derived from
VersionControlObject and applying the
[VersionControlAttribute](VersionControl.VersionControlAttribute.html).

    
    
    using UnityEditor.VersionControl;
    using UnityEngine;  
      
    [VersionControl("Custom")]
    public class CustomVersionControlObject : [VersionControlObject](VersionControl.VersionControlObject.html)
    {
        public override void OnActivate()
        {
            [Debug.Log](Debug.Log.html)("Custom VCS activated.");
        }  
      
        public override void OnDeactivate()
        {
            [Debug.Log](Debug.Log.html)("Custom VCS deactivated.");
        }
    }
    

Using the example above, a new VCS option called _Custom_ will show up in
Version Control settings window. You should only perform VCS operations when a
VersionControlObject is activated.
[OnActivate](VersionControl.VersionControlObject.OnActivate.html) and
[OnDeactivate](VersionControl.VersionControlObject.OnDeactivate.html) methods
are called on your class to notify your code about the change.  
  
Any persistent settings that must survive between Unity sessions (for example,
the username or password) must be handled either by the underlying VCS, by
using [EditorUserSettings](EditorUserSettings.html), or stored in a file. This
is because the VersionControlObject is not serialized to disk and a new
instance is created every time Unity starts up or when the VCS is activated.  
  
The VersionControlObject is derived from
[ScriptableObject](ScriptableObject.html). This makes [domain
reloading](../Manual/domain-reloading.html) handling simpler. You can add
[OnEnable](ScriptableObject.OnEnable.html) method to restore the state if
needed.  
  
You can use [AssetModificationProcessor](AssetModificationProcessor.html) and
[AssetPostprocessor.OnPostprocessAllAssets](AssetPostprocessor.OnPostprocessAllAssets.html)
to get notifications from Unity when it wants to edit, add or remove assets.  
  
Additional resources:
[VersionControlAttribute](VersionControl.VersionControlAttribute.html),
[VersionControlManager](VersionControl.VersionControlManager.html),
[EditorUserSettings](EditorUserSettings.html),
[ScriptableObject](ScriptableObject.html),
[AssetModificationProcessor](AssetModificationProcessor.html),
[AssetPostprocessor](AssetPostprocessor.html).

### Properties

[isConnected](VersionControl.VersionControlObject-isConnected.html)| Tests
whether the VersionControlObject is connected to an underlying version control
system.  
---|---  
  
### Public Methods

[GetExtension](VersionControl.VersionControlObject.GetExtension.html)| Gets
optional extension object.  
---|---  
[OnActivate](VersionControl.VersionControlObject.OnActivate.html)| Called when
your version control system is activated.  
[OnDeactivate](VersionControl.VersionControlObject.OnDeactivate.html)| Called
when your version control system is deactivated.  
[Refresh](VersionControl.VersionControlObject.Refresh.html)| Called when the
cached state should be discarded and the new state should be retrieved from
the underlying VCS.  
  
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

