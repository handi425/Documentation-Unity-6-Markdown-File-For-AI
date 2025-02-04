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

# Tilemap

class in UnityEngine.Tilemaps

/

Inherits from:[GridLayout](GridLayout.html)

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

The Tilemap stores [Sprite](Sprite.html)s in a layout marked by a
[Grid](Grid.html) component.

### Properties

[animationFrameRate](Tilemaps.Tilemap-animationFrameRate.html)| The frame rate
for all Tile animations in the Tilemap.  
---|---  
[cellBounds](Tilemaps.Tilemap-cellBounds.html)| Returns the boundaries of the
Tilemap in cell size.  
[color](Tilemaps.Tilemap-color.html)| The color of the Tilemap layer.  
[editorPreviewOrigin](Tilemaps.Tilemap-editorPreviewOrigin.html)| The origin
of the Tilemap in cell position inclusive of editor preview Tiles.  
[editorPreviewSize](Tilemaps.Tilemap-editorPreviewSize.html)| The size of the
Tilemap in cells inclusive of editor preview Tiles.  
[layoutGrid](Tilemaps.Tilemap-layoutGrid.html)| Gets the Grid associated with
this Tilemap.  
[localBounds](Tilemaps.Tilemap-localBounds.html)| Returns the boundaries of
the Tilemap in local space size.  
[orientation](Tilemaps.Tilemap-orientation.html)| Orientation of the Tiles in
the Tilemap.  
[orientationMatrix](Tilemaps.Tilemap-orientationMatrix.html)| Orientation
Matrix of the orientation of the Tiles in the Tilemap.  
[origin](Tilemaps.Tilemap-origin.html)| The origin of the Tilemap in cell
position.  
[size](Tilemaps.Tilemap-size.html)| The size of the Tilemap in cells.  
[tileAnchor](Tilemaps.Tilemap-tileAnchor.html)| Gets the anchor point of Tiles
in the Tilemap.  
  
### Public Methods

[AddTileAnimationFlags](Tilemaps.Tilemap.AddTileAnimationFlags.html)| Adds the
TileAnimationFlags onto the Tile at the given position.  
---|---  
[AddTileFlags](Tilemaps.Tilemap.AddTileFlags.html)| Adds the TileFlags onto
the Tile at the given position.  
[BoxFill](Tilemaps.Tilemap.BoxFill.html)| Does a box fill with the given Tile
on the Tilemap. Starts from given coordinates and fills the limits from start
to end (inclusive).  
[ClearAllEditorPreviewTiles](Tilemaps.Tilemap.ClearAllEditorPreviewTiles.html)|
Clears all editor preview Tiles that are placed in the Tilemap.  
[ClearAllTiles](Tilemaps.Tilemap.ClearAllTiles.html)| Clears all Tiles that
are placed in the Tilemap.  
[CompressBounds](Tilemaps.Tilemap.CompressBounds.html)| Compresses the origin
and size of the Tilemap to bounds where Tiles exist.  
[ContainsTile](Tilemaps.Tilemap.ContainsTile.html)| Returns true if the
Tilemap contains the given Tile. Returns false if not.  
[DeleteCells](Tilemaps.Tilemap.DeleteCells.html)| Removes cells from within
the Tilemap's bounds.  
[EditorPreviewBoxFill](Tilemaps.Tilemap.EditorPreviewBoxFill.html)| Does an
editor preview of a box fill with the given Tile on the Tilemap. Starts from
given coordinates and fills the limits from start to end (inclusive).  
[EditorPreviewFloodFill](Tilemaps.Tilemap.EditorPreviewFloodFill.html)| Does
an editor preview of a flood fill with the given Tile to place. on the Tilemap
starting from the given coordinates.  
[FloodFill](Tilemaps.Tilemap.FloodFill.html)| Does a flood fill with the given
Tile to place. on the Tilemap starting from the given coordinates.  
[GetAnimationFrame](Tilemaps.Tilemap.GetAnimationFrame.html)| Retrieves the
current animation frame for a Tile at the given position.  
[GetAnimationFrameCount](Tilemaps.Tilemap.GetAnimationFrameCount.html)|
Retrieves the number of animation frames for a Tile at the given position.  
[GetAnimationTime](Tilemaps.Tilemap.GetAnimationTime.html)| Retrieves the
current running animation time for a Tile at the given position.  
[GetCellCenterLocal](Tilemaps.Tilemap.GetCellCenterLocal.html)| Gets the
logical center coordinate of a Grid cell in local space. The logical center
for a cell of the Tilemap is defined by the Tile Anchor of the Tilemap.  
[GetCellCenterWorld](Tilemaps.Tilemap.GetCellCenterWorld.html)| Gets the
logical center coordinate of a Grid cell in world space. The logical center
for a cell of the Tilemap is defined by the Tile Anchor of the Tilemap.  
[GetColliderType](Tilemaps.Tilemap.GetColliderType.html)| Gets the Collider
type of a Tile given the XYZ coordinates of a cell in the Tilemap.  
[GetColor](Tilemaps.Tilemap.GetColor.html)| Gets the Color of a Tile given the
XYZ coordinates of a cell in the Tilemap.  
[GetEditorPreviewColor](Tilemaps.Tilemap.GetEditorPreviewColor.html)| Gets the
Color of an editor preview Tile given the XYZ coordinates of a cell in the
Tilemap.  
[GetEditorPreviewSprite](Tilemaps.Tilemap.GetEditorPreviewSprite.html)| Gets
the Sprite used in an editor preview Tile given the XYZ coordinates of a cell
in the Tilemap.  
[GetEditorPreviewTile](Tilemaps.Tilemap.GetEditorPreviewTile.html)| Gets the
editor preview Tile at the given XYZ coordinates of a cell in the Tilemap.  
[GetEditorPreviewTileFlags](Tilemaps.Tilemap.GetEditorPreviewTileFlags.html)|
Gets the TileFlags of the editor preview Tile at the given position.  
[GetEditorPreviewTransformMatrix](Tilemaps.Tilemap.GetEditorPreviewTransformMatrix.html)|
Gets the transform matrix of an editor preview Tile given the XYZ coordinates
of a cell in the Tilemap.  
[GetInstantiatedObject](Tilemaps.Tilemap.GetInstantiatedObject.html)| Gets the
GameObject instantiated by a Tile given the XYZ coordinates of a cell in the
Tilemap.  
[GetObjectToInstantiate](Tilemaps.Tilemap.GetObjectToInstantiate.html)| Gets
the GameObject which will be instantiated by a Tile given the XYZ coordinates
of a cell in the Tilemap.  
[GetSprite](Tilemaps.Tilemap.GetSprite.html)| Gets the Sprite used in a Tile
given the XYZ coordinates of a cell in the Tilemap.  
[GetTile](Tilemaps.Tilemap.GetTile.html)| Gets the Tile at the given XYZ
coordinates of a cell in the Tilemap.  
[GetTileAnimationFlags](Tilemaps.Tilemap.GetTileAnimationFlags.html)| Gets the
TileAnimationFlags of the Tile at the given position.  
[GetTileFlags](Tilemaps.Tilemap.GetTileFlags.html)| Gets the TileFlags of the
Tile at the given position.  
[GetTilesBlock](Tilemaps.Tilemap.GetTilesBlock.html)| Retrieves an array of
Tiles with the given bounds.  
[GetTilesBlockNonAlloc](Tilemaps.Tilemap.GetTilesBlockNonAlloc.html)|
Retrieves an array of Tiles with the given bounds.  
[GetTilesRangeCount](Tilemaps.Tilemap.GetTilesRangeCount.html)| Retrieves the
number of Tiles within the given range, inclusive of the Cells at both the
starting position and the ending positions. This method begins at the given
starting position and iterates through all available Z Positions, then
iterates through the X and Y positions until it reaches the ending position.  
[GetTilesRangeNonAlloc](Tilemaps.Tilemap.GetTilesRangeNonAlloc.html)|
Retrieves an array of Tiles within the given range, inclusive of the Cells at
both the starting position and the ending positions. This method begins at the
given starting position and iterates through all available Z Positions, then
iterates through the X and Y positions until it reaches the ending position.  
[GetTransformMatrix](Tilemaps.Tilemap.GetTransformMatrix.html)| Gets the
transform matrix of a Tile given the XYZ coordinates of a cell in the Tilemap.  
[GetUsedSpritesCount](Tilemaps.Tilemap.GetUsedSpritesCount.html)| Gets the
total number of different Sprites used in the Tilemap.  
[GetUsedSpritesNonAlloc](Tilemaps.Tilemap.GetUsedSpritesNonAlloc.html)| Fills
the given array with the total number of different Sprites used in the Tilemap
and returns the number of Sprites filled.  
[GetUsedTilesCount](Tilemaps.Tilemap.GetUsedTilesCount.html)| Gets the total
number of different Tiles used in the Tilemap.  
[GetUsedTilesNonAlloc](Tilemaps.Tilemap.GetUsedTilesNonAlloc.html)| Fills the
given array with the total number of different Tiles used in the Tilemap and
returns the number of Tiles filled.  
[HasEditorPreviewTile](Tilemaps.Tilemap.HasEditorPreviewTile.html)| Returns
whether there is an editor preview Tile at the position.  
[HasTile](Tilemaps.Tilemap.HasTile.html)| Returns whether there is a Tile at
the position.  
[InsertCells](Tilemaps.Tilemap.InsertCells.html)| Inserts cells into the
Tilemap.  
[RefreshAllTiles](Tilemaps.Tilemap.RefreshAllTiles.html)| Refreshes all Tiles
in the Tilemap. The Tilemap will retrieve the rendering data, animation data
and other data for all tiles and update all relevant components.  
[RefreshTile](Tilemaps.Tilemap.RefreshTile.html)| Refreshes a Tile at the
given XYZ coordinates of a cell in the Tilemap.  
[RemoveTileAnimationFlags](Tilemaps.Tilemap.RemoveTileAnimationFlags.html)|
Removes the TileAnimationFlags from the Tile at the given position.  
[RemoveTileFlags](Tilemaps.Tilemap.RemoveTileFlags.html)| Removes the
TileFlags from the Tile at the given position.  
[ResizeBounds](Tilemaps.Tilemap.ResizeBounds.html)| Resizes Tiles in the
Tilemap to bounds defined by origin and size.  
[SetAnimationFrame](Tilemaps.Tilemap.SetAnimationFrame.html)| Sets the current
animation frame for a Tile at the given position.  
[SetAnimationTime](Tilemaps.Tilemap.SetAnimationTime.html)| Sets the running
animation time for a Tile at the given position.  
[SetColliderType](Tilemaps.Tilemap.SetColliderType.html)| Sets the Collider
type of a Tile given the XYZ coordinates of a cell in the Tilemap.  
[SetColor](Tilemaps.Tilemap.SetColor.html)| Sets the color of a Tile given the
XYZ coordinates of a cell in the Tilemap.  
[SetEditorPreviewColor](Tilemaps.Tilemap.SetEditorPreviewColor.html)| Sets the
color of an editor preview Tile given the XYZ coordinates of a cell in the
Tilemap.  
[SetEditorPreviewTile](Tilemaps.Tilemap.SetEditorPreviewTile.html)| Sets an
editor preview Tile given the XYZ coordinates of a cell in the Tilemap.  
[SetEditorPreviewTransformMatrix](Tilemaps.Tilemap.SetEditorPreviewTransformMatrix.html)|
Sets the transform matrix of an editor preview Tile given the XYZ coordinates
of a cell in the Tilemap.  
[SetTile](Tilemaps.Tilemap.SetTile.html)| Sets a Tile at the given XYZ
coordinates of a cell in the Tilemap.  
[SetTileAnimationFlags](Tilemaps.Tilemap.SetTileAnimationFlags.html)| Sets the
TileAnimationFlags onto the Tile at the given position.  
[SetTileFlags](Tilemaps.Tilemap.SetTileFlags.html)| Sets the TileFlags onto
the Tile at the given position.  
[SetTiles](Tilemaps.Tilemap.SetTiles.html)| Sets an array of Tiles at the
given XYZ coordinates of the corresponding cells in the Tilemap.  
[SetTilesBlock](Tilemaps.Tilemap.SetTilesBlock.html)| Fills bounds with array
of Tiles.  
[SetTransformMatrix](Tilemaps.Tilemap.SetTransformMatrix.html)| Sets the
transform matrix of a Tile given the XYZ coordinates of a cell in the Tilemap.  
[SwapTile](Tilemaps.Tilemap.SwapTile.html)| Swaps all existing Tiles of
changeTile to newTile and refreshes all the swapped Tiles.  
  
### Events

[loopEndedForTileAnimation](Tilemaps.Tilemap-loopEndedForTileAnimation.html)|
Callback when Tiles on a Tilemap have reached the end of their loop for their
Tile Animation.  
---|---  
[tilemapPositionsChanged](Tilemaps.Tilemap-tilemapPositionsChanged.html)|
Callback when Tiles on a Tilemap have changed.  
[tilemapTileChanged](Tilemaps.Tilemap-tilemapTileChanged.html)| Callback when
Tiles on a Tilemap have changed.  
  
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

