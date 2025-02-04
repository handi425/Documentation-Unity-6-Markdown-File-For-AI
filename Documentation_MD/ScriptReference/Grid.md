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

# Grid

class in UnityEngine

/

Inherits from:[GridLayout](GridLayout.html)

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

Grid is the base class for plotting a layout of uniformly spaced points and
lines.

The Grid component stores dimensional data of the layout of the grid and
provides helper functions to retrieve information about the grid, such as the
conversion between the cell location and local space location of items within
the grid.  
  
The layout of the Grid component is in the XY plane with the origin of the
grid always beginning at (0, 0) and the X and Y coordinates of the grid only
as positive values.  
  
Implements the interface [GridLayout](GridLayout.html).

### Properties

[cellGap](Grid-cellGap.html)| The size of the gap between each cell in the
Grid.  
---|---  
[cellLayout](Grid-cellLayout.html)| The layout of the cells in the Grid.  
[cellSize](Grid-cellSize.html)| The size of each cell in the Grid.  
[cellSwizzle](Grid-cellSwizzle.html)| The cell swizzle for the Grid.  
  
### Public Methods

[GetCellCenterLocal](Grid.GetCellCenterLocal.html)| Get the logical center
coordinate of a grid cell in local space.  
---|---  
[GetCellCenterWorld](Grid.GetCellCenterWorld.html)| Get the logical center
coordinate of a grid cell in world space.  
  
### Static Methods

[InverseSwizzle](Grid.InverseSwizzle.html)| Does the inverse swizzle of the
given position for given swizzle order.  
---|---  
[Swizzle](Grid.Swizzle.html)| Swizzles the given position with the given
swizzle order.  
  
### Inherited Members

### Properties

[enabled](Behaviour-enabled.html)| Enabled Behaviours are Updated, disabled
Behaviours are not.  
---|---  
[isActiveAndEnabled](Behaviour-isActiveAndEnabled.html)| Reports whether a
GameObject and its associated Behaviour is active and enabled.  
[gameObject](Component-gameObject.html)| The game object this component is
attached to. A component is always attached to a game object.  
[tag](Component-tag.html)| The tag of this game object.  
[transform](Component-transform.html)| The Transform attached to this
GameObject.  
[cellGap](GridLayout-cellGap.html)| The size of the gap between each cell in
the layout.  
[cellLayout](GridLayout-cellLayout.html)| The layout of the cells.  
[cellSize](GridLayout-cellSize.html)| The size of each cell in the layout.  
[cellSwizzle](GridLayout-cellSwizzle.html)| The cell swizzle for the layout.  
[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[BroadcastMessage](Component.BroadcastMessage.html)| Calls the method named
methodName on every MonoBehaviour in this game object or any of its children.  
---|---  
[CompareTag](Component.CompareTag.html)| Checks the GameObject's tag against
the defined tag.  
[GetComponent](Component.GetComponent.html)| Gets a reference to a component
of type T on the same GameObject as the component specified.  
[GetComponentInChildren](Component.GetComponentInChildren.html)| Gets a
reference to a component of type T on the same GameObject as the component
specified, or any child of the GameObject.  
[GetComponentIndex](Component.GetComponentIndex.html)| Gets the index of the
component on its parent GameObject.  
[GetComponentInParent](Component.GetComponentInParent.html)| Gets a reference
to a component of type T on the same GameObject as the component specified, or
any parent of the GameObject.  
[GetComponents](Component.GetComponents.html)| Gets references to all
components of type T on the same GameObject as the component specified.  
[GetComponentsInChildren](Component.GetComponentsInChildren.html)| Gets
references to all components of type T on the same GameObject as the component
specified, and any child of the GameObject.  
[GetComponentsInParent](Component.GetComponentsInParent.html)| Gets references
to all components of type T on the same GameObject as the component specified,
and any parent of the GameObject.  
[SendMessage](Component.SendMessage.html)| Calls the method named methodName
on every MonoBehaviour in this game object.  
[SendMessageUpwards](Component.SendMessageUpwards.html)| Calls the method
named methodName on every MonoBehaviour in this game object and on every
ancestor of the behaviour.  
[TryGetComponent](Component.TryGetComponent.html)| Gets the component of the
specified type, if it exists.  
[CellToLocal](GridLayout.CellToLocal.html)| Converts a cell position to local
position space.  
[CellToLocalInterpolated](GridLayout.CellToLocalInterpolated.html)| Converts
an interpolated cell position in floats to local position space.  
[CellToWorld](GridLayout.CellToWorld.html)| Converts a cell position to world
position space.  
[GetBoundsLocal](GridLayout.GetBoundsLocal.html)| Returns the local bounds for
a cell at the location.  
[GetLayoutCellCenter](GridLayout.GetLayoutCellCenter.html)| Get the default
center coordinate of a cell for the set layout of the Grid.  
[LocalToCell](GridLayout.LocalToCell.html)| Converts a local position to cell
position.  
[LocalToCellInterpolated](GridLayout.LocalToCellInterpolated.html)| Converts a
local position to cell position.  
[LocalToWorld](GridLayout.LocalToWorld.html)| Converts a local position to
world position.  
[WorldToCell](GridLayout.WorldToCell.html)| Converts a world position to cell
position.  
[WorldToLocal](GridLayout.WorldToLocal.html)| Converts a world position to
local position.  
[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
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

