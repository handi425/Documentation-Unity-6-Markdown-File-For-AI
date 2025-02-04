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

# ScriptableObject

class in UnityEngine

/

Inherits from:[Object](Object.html)

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

[Switch to Manual](../Manual/class-ScriptableObject.html "Go to
ScriptableObject Component in the Manual")

### Description

A class you can derive from if you want to create objects that live
independently of GameObjects.

Use ScriptableObjects to centralise data in a way that can be conveniently
accessed from scenes and assets within a project.  
  
Instantiate ScriptableObject objects with
[CreateInstance](ScriptableObject.CreateInstance.html).  
  
You can save ScriptableObjects to asset files either from the Editor UI (see
[CreateAssetMenuAttribute](CreateAssetMenuAttribute.html)), or by calling
[AssetDatabase.CreateAsset](AssetDatabase.CreateAsset.html) from a script. You
can also generate ScriptableObjects as an output from a
[ScriptedImporter](AssetImporters.ScriptedImporter.html). See
[AssetImportContext.AddObjectToAsset](AssetImporters.AssetImportContext.AddObjectToAsset.html).  
  
If a `ScriptableObject` has not been saved to an asset, and it is referenced
from an object in a scene, Unity serializes it directly into the scene file.
For ScriptableObjects that have only a single persistent instance within a
project, use the [ScriptableSingleton<T0>](ScriptableSingleton_1.html) base
class.  
  
Access previously saved objects using [AssetDatabase](AssetDatabase.html), for
example [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html).
When a ScriptableObject is referenced from a field on a
[MonoBehaviour](MonoBehaviour.html), the ScriptableObject is automatically
loaded, so a script can simply use the value of the field to reach it.  
  
The C# fields of a `ScriptableObject` are serialized exactly like fields on a
MonoBehaviour, refer to [Script Serialization](../Manual/script-
serialization.html) for details. Classes that include big arrays, or other
potentially large data, should be declared with the
[PreferBinarySerialization](PreferBinarySerialization.html) attribute, because
YAML is not an efficient representation for that sort of data.  
  
Calling `Destroy` on a `ScriptableObject` releases native resources associated
with it but the object stays in memory until garbage collected. Objects in
this detached state will appear to be null despite not really being so.
However, this class doesn't support the [null-conditional operator
](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/language-
specification/expressions#null-conditional-operator) (**?.**) and the [null-
coalescing operator ](https://docs.microsoft.com/en-us/dotnet/csharp/language-
reference/language-specification/expressions#the-null-coalescing-
operator)(**??**).  
  
The following example demonstrates a typical use of a ScriptableObject:
different types of vehicle parameters are represented in the fields of a
VehicleTypeInfo class, derived from ScriptableObject. Each type of vehicle
would have its own asset file, with the parameter values set appropriately for
the type. Each instance of the vehicle in the game would have a reference to
the asset corresponding to its type, rather than keeping its own redundant
copy of each parameter. This design makes it convenient to tweak vehicle
behaviour in a central location. It is also good for performance, especially
in cases where the size of the shared data is substantial.  
  
The first script of the example implements a class derived from
ScriptableObject.

    
    
    using UnityEngine;  
      
    [CreateAssetMenu]
    public class VehicleTypeInfo : [ScriptableObject](ScriptableObject.html)
    {
        // Class that represents a specific type of vehicle
        [Range(0.1f, 100f)]
        public float m_MaxSpeed = 0.1f;  
      
        [Range(0.1f, 10f)]
        public float m_MaxAcceration = 0.1f;  
      
        // This class could have many other vehicle parameters, such as Turning Radius, Range, Damage etc
    }
    

The second script implements a MonoBehaviour that uses the ScriptableObject.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class VehicleInstance : [MonoBehaviour](MonoBehaviour.html)
    {
        // Snippet of a [MonoBehaviour](MonoBehaviour.html) that would control motion of a specific vehicle.
        // In [PlayMode](PlayMode.html) it accelerates up to the maximum speed permitted by its type  
      
        [Range(0f, 200f)]
        public float m_CurrentSpeed;  
      
        [Range(0f, 50f)]
        public float m_Acceleration;  
      
        // Reference to the [ScriptableObject](ScriptableObject.html) asset
        public VehicleTypeInfo m_VehicleType;  
      
        public void Initialize(VehicleTypeInfo vehicleType)
        {
            m_VehicleType = vehicleType;
            m_CurrentSpeed = 0f;
            m_Acceleration = [Random.Range](Random.Range.html)(0.05f, m_VehicleType.m_MaxAcceration);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            m_CurrentSpeed += m_Acceleration * [Time.deltaTime](Time-deltaTime.html);  
      
            // Use parameter from the [ScriptableObject](ScriptableObject.html) to control the behaviour of the Vehicle
            if (m_VehicleType && m_VehicleType.m_MaxSpeed < m_CurrentSpeed)
                m_CurrentSpeed = m_VehicleType.m_MaxSpeed;  
      
            gameObject.transform.position += gameObject.transform.forward * [Time.deltaTime](Time-deltaTime.html) * m_CurrentSpeed;
        }
    }  
      
    public class ScriptableObjectVehicleExample
    {
        [[MenuItem](MenuItem.html)("Example/Setup [ScriptableObject](ScriptableObject.html) Vehicle Example")]
        static void MenuCallback()
        {
            // This example programmatically performs steps that would typically be performed from the [Editor](Editor.html)'s user interface
            // to creates a simple demonstration.  When going into Playmode the three objects will move according to the limits
            // set by their vehicle type.  
      
            // Step 1 - Create or reload the assets that store each VehicleTypeInfo object.
            VehicleTypeInfo wagon = [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<VehicleTypeInfo>("Assets/VehicleTypeWagon.asset");
            if (wagon == null)
            {
                // Create and save [ScriptableObject](ScriptableObject.html) because it doesn't exist yet
                wagon = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<VehicleTypeInfo>();
                wagon.m_MaxSpeed = 5f;
                wagon.m_MaxAcceration = 0.5f;
                [AssetDatabase.CreateAsset](AssetDatabase.CreateAsset.html)(wagon, "Assets/VehicleTypeWagon.asset");
            }  
      
            VehicleTypeInfo cruiser = [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<VehicleTypeInfo>("Assets/VehicleTypeCruiser.asset");
            if (cruiser == null)
            {
                cruiser = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<VehicleTypeInfo>();
                cruiser.m_MaxSpeed = 75f;
                cruiser.m_MaxAcceration = 2f;
                [AssetDatabase.CreateAsset](AssetDatabase.CreateAsset.html)(cruiser, "Assets/VehicleTypeCruiser.asset");
            }  
      
            // Step 2 - Create some example vehicles in the current scene
            {
                var vehicle = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Sphere](PrimitiveType.Sphere.html));
                vehicle.name = "Wagon1";
                var vehicleBehaviour = vehicle.AddComponent<VehicleInstance>();
                vehicleBehaviour.Initialize(wagon);
            }  
      
            {
                var vehicle = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Sphere](PrimitiveType.Sphere.html));
                vehicle.name = "Wagon2";
                var vehicleBehaviour = vehicle.AddComponent<VehicleInstance>();
                vehicleBehaviour.Initialize(wagon);
            }  
      
            {
                var vehicle = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Cube](PrimitiveType.Cube.html));
                vehicle.name = "Cruiser1";
                var vehicleBehaviour = vehicle.AddComponent<VehicleInstance>();
                vehicleBehaviour.Initialize(cruiser);
            }
        }
    }
    

### Static Methods

[CreateInstance](ScriptableObject.CreateInstance.html)| Creates an instance of
a scriptable object.  
---|---  
  
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

