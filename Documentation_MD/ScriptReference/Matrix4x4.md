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

# Matrix4x4

struct in UnityEngine

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

[ ]()

### Description

A standard 4x4 transformation matrix.

A transformation matrix can perform arbitrary linear 3D transformations (i.e.
translation, rotation, scale, shear etc.) and perspective transformations
using homogenous coordinates. You rarely use matrices in scripts; most often
using [Vector3](Vector3.html)s, [Quaternion](Quaternion.html)s and
functionality of [Transform](Transform.html) class is more straightforward.
Plain matrices are used in special cases like setting up nonstandard camera
projection.  
  
In Unity, several [Transform](Transform.html), [Camera](Camera.html),
[Material](Material.html), [Graphics](Graphics.html) and [GL](GL.html)
functions use Matrix4x4.  
  
Matrices in Unity are column major; i.e. the position of a transformation
matrix is in the last column, and the first three columns contain x, y, and
z-axes. Data is accessed as: `row + (column*4)`. Matrices can be indexed like
2D arrays but note that in an expression like `mat[a, b]`, `a` refers to the
row index, while `b` refers to the column index.

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // get matrix from the [Transform](Transform.html)
            var matrix = transform.localToWorldMatrix;
            // get position from the last column
            var position = new [Vector3](Vector3.html)(matrix[0,3], matrix[1,3], matrix[2,3]);
            [Debug.Log](Debug.Log.html)("[Transform](Transform.html) position from matrix is: " + position);
        }
    }
    

### Static Properties

[identity](Matrix4x4-identity.html)| Returns the identity matrix (Read Only).  
---|---  
[zero](Matrix4x4-zero.html)| Returns a matrix with all elements set to zero
(Read Only).  
  
### Properties

[decomposeProjection](Matrix4x4-decomposeProjection.html)| This property takes
a projection matrix and returns the six plane coordinates that define a
projection frustum.  
---|---  
[determinant](Matrix4x4-determinant.html)| The determinant of the matrix.
(Read Only)  
[inverse](Matrix4x4-inverse.html)| The inverse of this matrix. (Read Only)  
[isIdentity](Matrix4x4-isIdentity.html)| Checks whether this is an identity
matrix. (Read Only)  
[lossyScale](Matrix4x4-lossyScale.html)| Attempts to get a scale value from
the matrix. (Read Only)  
[rotation](Matrix4x4-rotation.html)| Attempts to get a rotation quaternion
from this matrix.  
[this[int,int]](Matrix4x4.Index_operator.html)| Access element at [row,
column].  
[transpose](Matrix4x4-transpose.html)| Returns the transpose of this matrix
(Read Only).  
  
### Public Methods

[GetColumn](Matrix4x4.GetColumn.html)| Get a column of the matrix.  
---|---  
[GetPosition](Matrix4x4.GetPosition.html)| Get position vector from the
matrix.  
[GetRow](Matrix4x4.GetRow.html)| Returns a row of the matrix.  
[MultiplyPoint](Matrix4x4.MultiplyPoint.html)| Transforms a position by this
matrix (generic).  
[MultiplyPoint3x4](Matrix4x4.MultiplyPoint3x4.html)| Transforms a position by
this matrix (fast).  
[MultiplyVector](Matrix4x4.MultiplyVector.html)| Transforms a direction by
this matrix.  
[SetColumn](Matrix4x4.SetColumn.html)| Sets a column of the matrix.  
[SetRow](Matrix4x4.SetRow.html)| Sets a row of the matrix.  
[SetTRS](Matrix4x4.SetTRS.html)| Sets this matrix to a translation, rotation
and scaling matrix.  
[ToString](Matrix4x4.ToString.html)| Returns a formatted string for this
matrix.  
[TransformPlane](Matrix4x4.TransformPlane.html)| Returns a plane that is
transformed in space.  
[ValidTRS](Matrix4x4.ValidTRS.html)| Checks if this matrix is a valid
transform matrix.  
  
### Static Methods

[Frustum](Matrix4x4.Frustum.html)| This function returns a projection matrix
with viewing frustum that has a near plane defined by the coordinates that
were passed in.  
---|---  
[Inverse3DAffine](Matrix4x4.Inverse3DAffine.html)| Computes the inverse of a
3D affine matrix.  
[LookAt](Matrix4x4.LookAt.html)| Create a "look at" matrix.  
[Ortho](Matrix4x4.Ortho.html)| Create an orthogonal projection matrix.  
[Perspective](Matrix4x4.Perspective.html)| Create a perspective projection
matrix.  
[Rotate](Matrix4x4.Rotate.html)| Creates a rotation matrix.  
[Scale](Matrix4x4.Scale.html)| Creates a scaling matrix.  
[Translate](Matrix4x4.Translate.html)| Creates a translation matrix.  
[TRS](Matrix4x4.TRS.html)| Creates a translation, rotation and scaling matrix.  
  
### Operators

[operator *](Matrix4x4-operator_multiply.html)| Multiplies two matrices.  
---|---  
  
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

