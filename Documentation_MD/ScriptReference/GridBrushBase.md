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

# GridBrushBase

class in UnityEngine

/

Inherits from:[ScriptableObject](ScriptableObject.html)

/

Implemented in:[UnityEngine.TilemapModule](UnityEngine.TilemapModule.html)

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

Base class for authoring data on a grid with grid painting tools like paint,
erase, pick, select and fill.

Inheriting this class and/or creating brush asset instances from your
inherited class, you can create custom brushes which react to high level grid
events like paint, erase, pick, select and fill.

    
    
    using UnityEngine;  
      
    // Paints two Prefabs in checkerboard pattern
    [CreateAssetMenu]
    public class CheckerboardBrush : [GridBrushBase](GridBrushBase.html)
    {
        public [GameObject](GameObject.html) prefabA;
        public [GameObject](GameObject.html) prefabB;  
      
        public override void Paint([GridLayout](GridLayout.html) grid, [GameObject](GameObject.html) brushTarget, [Vector3Int](Vector3Int.html) position)
        {
            bool evenCell = [Mathf.Abs](Mathf.Abs.html)(position.y + position.x) % 2 > 0;
            [GameObject](GameObject.html) toBeInstantiated = evenCell ? prefabA : prefabB;  
      
            if (toBeInstantiated != null)
            {
                [GameObject](GameObject.html) newInstance = Instantiate(toBeInstantiated, grid.CellToWorld(position), [Quaternion.identity](Quaternion-identity.html));
                newInstance.transform.SetParent(brushTarget.transform);
            }
        }
    }
    

### Public Methods

[BoxErase](GridBrushBase.BoxErase.html)| Erases data on a grid within the
given bounds.  
---|---  
[BoxFill](GridBrushBase.BoxFill.html)| Box fills tiles and GameObjects into
given bounds within the selected layers.  
[ChangeZPosition](GridBrushBase.ChangeZPosition.html)| Changes the Z position
of the GridBrushBase.  
[Erase](GridBrushBase.Erase.html)| Erases data on a grid within the given
bounds.  
[Flip](GridBrushBase.Flip.html)| Flips the grid brush in the given FlipAxis.  
[FloodFill](GridBrushBase.FloodFill.html)| Flood fills data onto a grid given
the starting coordinates of the cell.  
[Move](GridBrushBase.Move.html)| Move is called when user moves the area
previously selected with the selection marquee.  
[MoveEnd](GridBrushBase.MoveEnd.html)| MoveEnd is called when user has ended
the move of the area previously selected with the selection marquee.  
[MoveStart](GridBrushBase.MoveStart.html)| MoveEnd is called when user starts
moving the area previously selected with the selection marquee.  
[Paint](GridBrushBase.Paint.html)| Paints data into a grid within the given
bounds.  
[Pick](GridBrushBase.Pick.html)| Picks data from a grid given the coordinates
of the cells.  
[ResetZPosition](GridBrushBase.ResetZPosition.html)| Resets Z position changes
of the GridBrushBase.  
[Rotate](GridBrushBase.Rotate.html)| Rotates all tiles on the grid brush with
the given RotationDirection.  
[Select](GridBrushBase.Select.html)| Select an area of a grid.  
  
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

